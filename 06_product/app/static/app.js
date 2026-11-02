"use strict";
// All user content and model output goes through textContent, never concatenated into innerHTML, to prevent injection.
const $app = document.getElementById("app");
const T = {fulfilled:"Reported done in the meeting",partial_or_rescheduled:"Unfinished or rescheduled",abandoned:"Dropped",not_mentioned:"Not mentioned"};
const STR = {committed:"Committed",tentative:"Might do",suggestion:"Just a suggestion",hypothesis:"Speculation"};
const KIND = {group:"Group meeting",one_on_one:"1-on-1",partner:"Partner meeting",other:"Other"};
const STAGE = {queued:["Queued",10],transcribing:["Transcribing audio (longer recordings take a few minutes)",30],extracting:["Extracting tasks, decisions and results",60],reconciling:["Reconciling against items from the last meeting",85]};
const COLS = [["todo","To do"],["doing","In progress"],["done","Done"],["dropped","Dropped"]];

function h(tag, attrs, ...kids){
  const e=document.createElement(tag);
  for(const [k,v] of Object.entries(attrs||{})){
    if(v===null||v===undefined||v===false) continue;
    if(k.startsWith("on")) e.addEventListener(k.slice(2),v);
    else if(k==="class") e.className=v;
    else if(k==="value") e.value=v;
    else if(k==="disabled"||k==="checked"||k==="selected") e[k]=!!v;
    else e.setAttribute(k,v);
  }
  for(const c of kids.flat()){ if(c===null||c===undefined||c===false) continue; e.append(c.nodeType?c:String(c)); }
  return e;
}
function toast(m){const t=document.getElementById("toast");t.textContent=m;t.classList.add("on");clearTimeout(toast.t);toast.t=setTimeout(()=>t.classList.remove("on"),2600);}
async function api(path,opts={}){
  const o={...opts};
  if(o.json!==undefined){o.body=JSON.stringify(o.json);o.headers={"Content-Type":"application/json"};delete o.json;}
  let r;
  try{r=await fetch(path,o);}catch(e){throw new Error("Network connection failed. Please try again.");}
  const ct=r.headers.get("content-type")||"";
  const d=ct.includes("json")?await r.json():await r.text();
  if(!r.ok) throw new Error(d.error||d.detail&&JSON.stringify(d.detail)||"Request failed ("+r.status+")");
  return d;
}
const guard=fn=>async(...a)=>{try{return await fn(...a);}catch(e){toast(e.message);}};
function route(){
  const p=location.pathname.split("/").filter(Boolean);
  if(p[0]==="privacy") return {view:"privacy"};
  if(p[0]==="l") return {token:p[1],view:p[2]||"meetings",code:p[3]};
  return {view:"home"};
}
function go(path){history.pushState(null,"",path);render();}
window.addEventListener("popstate",()=>render());
let timer=null;
function stopPoll(){if(timer){clearTimeout(timer);timer=null;}}
function link(path,text,attrs={}){return h("a",{href:path,...attrs,onclick:e=>{e.preventDefault();go(path);}},text);}
function today(){const d=new Date();return new Date(d-d.getTimezoneOffset()*6e4).toISOString().slice(0,10);}
function say(token,name,props){}

async function render(){
  stopPoll();
  const r=route();
  try{
    if(r.view==="home") return renderHome();
    if(r.view==="privacy") return renderPrivacy();
    const led=await api(`/api/l/${r.token}`);
    document.title=`${led.name} · Meeting Ledger`;
    const body=h("main",{});
    $app.replaceChildren(topbar(r,led),body);
    if(r.view==="new") renderNew(body,r,led);
    else if(r.view==="m") await renderMeeting(body,r,led);
    else if(r.view==="tasks") await renderTasks(body,r,led);
    else if(r.view==="settings") renderSettings(body,r,led);
    else renderMeetings(body,r,led);
  }catch(e){
    $app.replaceChildren(h("main",{class:"narrow"},h("h1",{},"Can't open this ledger"),h("p",{},e.message),link("/","Back to home")));
  }
}
function topbar(r,led){
  const tab=(v,t,tid)=>link(`/l/${r.token}/${v}`,t,{class:(r.view===v||(v==="meetings"&&r.view==="m"))?"on":"","data-testid":tid});
  return h("header",{class:"top"},link("/","Meeting Ledger",{class:"brand"}),h("span",{class:"mute"},led.name),
    h("nav",{class:"tabs"},tab("meetings","Meetings","tab-meetings"),tab("tasks","Task board","tab-tasks"),tab("settings","Settings","tab-settings")),
    h("span",{class:"spacer"}),
    h("button",{"data-testid":"open-survey",onclick:()=>openSurvey(r.token)},"Give feedback"),
    h("button",{class:"primary","data-testid":"new-meeting",onclick:()=>go(`/l/${r.token}/new`)},"New meeting"));
}

function add(parent,...kids){for(const k of kids.flat()){if(k!==null&&k!==undefined&&k!==false)parent.append(k);}return parent;}
function renderPrivacy(){
  document.title="Privacy · Meeting Ledger";
  $app.replaceChildren(h("main",{class:"narrow","data-testid":"privacy"},h("h1",{},"Privacy"),
    h("h2",{},"Where your data goes"),h("p",{},"Meeting text is sent to the model service Anthropic for processing. Anthropic's official documentation governs its data policies. Audio is transcribed only on this server with a local model, deleted immediately after transcription, and never sent to third parties."),
    h("h2",{},"How long it's kept"),h("p",{},"Transcripts, tasks and feedback stay on the server until you delete the ledger on the Settings page. Deletion is permanent and can't be undone."),
    h("h2",{},"Who can see it"),h("p",{},"There is no account system. Anyone with the ledger link can view and edit it, so treat the link like a password and share it only with people who need it. There are currently no access logs. Whoever runs this deployment can access the database on the server."),
    h("h2",{},"What you need to do"),h("p",{},"Get the participants' consent before submitting. Don't submit unpublished sensitive data, sensitive personal information or anything covered by a confidentiality agreement."),
    h("p",{},link("/","Back to home"))));
}
function renderHome(){
  document.title="Meeting Ledger";
  const name=h("input",{placeholder:"e.g. Robot Learning Group weekly meeting","data-testid":"ledger-name",maxlength:60,"aria-label":"Ledger name",style:"flex:1;min-width:200px"});
  const members=h("input",{placeholder:"Member list, comma-separated (optional): Alice, Bob","data-testid":"ledger-members","aria-label":"Member list",style:"width:100%"});
  const create=guard(async()=>{
    if(!name.value.trim()) return toast("Give the ledger a name first");
    const d=await api("/api/ledgers",{method:"POST",json:{name:name.value,members:members.value.split(/[,，、]/)}});
    go(`/l/${d.token}/new`);
  });
  const sample=guard(async()=>{const d=await api("/api/sample",{method:"POST"});go(`/l/${d.token}/m/M3`);});
  $app.replaceChildren(h("main",{class:"narrow"},
    h("h1",{},"After the meeting, tasks land on the task board. At the next one, last meeting's items reconcile automatically."),
    h("p",{},"Upload a recording or paste text to get draft tasks with owners, due dates and quotes. Nothing is saved until you confirm it. When the next meeting says “it's half done” or “let's drop it for now”, the ledger automatically matches that back to the original task."),
    h("div",{class:"steps"},
      h("div",{class:"card"},h("strong",{},"1. Submit a meeting"),h("div",{class:"mute"},"Audio or text, mixed Chinese and English is fine")),
      h("div",{class:"card"},h("strong",{},"2. Confirm and assign"),h("div",{class:"mute"},"Every item links back to its quote. Anything not said stays blank, with no guessing")),
      h("div",{class:"card"},h("strong",{},"3. Reconcile automatically next time"),h("div",{class:"mute"},"See at a glance who said what and which items keep going unmentioned"))),
    h("div",{class:"card"},h("h2",{style:"margin-top:0"},"New ledger"),
      h("div",{class:"row"},name,h("button",{class:"primary","data-testid":"create-ledger",onclick:create},"Create")),
      h("div",{style:"margin-top:8px"},members),
      h("p",{class:"mute"},"No sign-up needed. A ledger is accessed through a private link, so keep it safe: anyone with the link can view and edit.")),
    h("p",{},h("button",{"data-testid":"try-sample",onclick:sample},"See the sample ledger first (fictional data, takes no time)")),
    h("p",{class:"mute"},"Meeting text is sent to a model service (Anthropic) for processing. Audio is transcribed on the server and deleted immediately afterward. Please get the participants' consent first. ",link("/privacy","Privacy"))));
}

function renderMeetings(body,r,led){
  body.classList.add("narrow");
  body.append(h("h1",{},"Meetings"));
  if(led.is_sample) body.append(h("div",{class:"banner"},"This is a sample ledger. The people and projects are fictional."));
  if(!led.meetings.length){
    body.append(h("div",{class:"card"},h("p",{},"No meetings yet. Submit your first meeting to get your first draft tasks."),h("button",{class:"primary",onclick:()=>go(`/l/${r.token}/new`)},"Submit your first meeting")));
    return;
  }
  for(const m of [...led.meetings].reverse()){
    body.append(h("div",{class:"card row","data-testid":"meeting-row"},
      h("div",{style:"flex:1;min-width:200px"},link(`/l/${r.token}/m/${m.code}`,`${m.date} · ${m.title||KIND[m.kind]}`),
        h("div",{class:"mute"},`${KIND[m.kind]} · ${m.source==="audio"?"Audio":"Text"}`)),
      m.status==="ready"?h("span",{class:"badge b-ok"},"Processed"):m.status==="failed"?h("span",{class:"badge b-bad"},"Failed"):h("span",{class:"badge b-warn"},"Processing")));
  }
}

function renderNew(body,r,led){
  body.classList.add("narrow");
  const date=h("input",{type:"date",value:today(),"data-testid":"meeting-date",id:"f-date"});
  const title=h("input",{placeholder:"Optional, e.g. Week 12 group meeting","data-testid":"meeting-title",id:"f-title",maxlength:120});
  const kind=h("select",{"data-testid":"meeting-kind",id:"f-kind"},Object.entries(KIND).map(([k,v])=>h("option",{value:k},v)));
  const text=h("textarea",{placeholder:"Paste the meeting text. These formats are supported:\n[00:01:02] Bob: I'll finish the run by Friday\nBob: I'll finish the run by Friday\nBob 21:03 (content on the next line, as in Feishu and WeChat exports)\nOr plain text with one sentence per line.\n\nOwner detection is much more accurate when speakers are included.","data-testid":"meeting-text",id:"f-text"});
  const file=h("input",{type:"file",accept:"audio/*,video/mp4,.m4a,.mp3,.wav,.txt,.md","data-testid":"meeting-file",id:"f-file"});
  const btn=h("button",{class:"primary","data-testid":"submit-meeting"},"Start processing");
  btn.onclick=guard(async()=>{
    const f=new FormData();
    f.append("meeting_date",date.value);f.append("title",title.value);f.append("kind",kind.value);f.append("text",text.value);
    if(file.files[0]) f.append("file",file.files[0]);
    btn.disabled=true;
    try{const d=await api(`/api/l/${r.token}/meetings`,{method:"POST",body:f});go(`/l/${r.token}/m/${d.code}`);}
    finally{btn.disabled=false;}
  });
  const prev=led.meetings.filter(m=>m.status==="ready").length;
  add(body,h("h1",{},"New meeting"),
    prev?h("div",{class:"banner ok"},`This is meeting #${prev+1}. Processing will automatically reconcile it against earlier items that are still open.`):h("p",{class:"mute"},"This is the first meeting, so only tasks will be extracted. From the second meeting on, the previous meeting's items are followed up automatically."),
    !led.asr?h("div",{class:"banner"},"Speech transcription isn't enabled on this deployment. Please paste text."):null,
    !led.model_ready&&!led.is_sample?h("div",{class:"banner err"},"This deployment doesn't have a model configured yet, so new meetings can't be processed for now."):null,
    h("div",{class:"card"},
      h("div",{class:"row"},h("div",{class:"field"},h("label",{for:"f-date"},"Meeting date (used to resolve phrases like “by Friday”)"),date),
        h("div",{class:"field"},h("label",{for:"f-kind"},"Type"),kind),
        h("div",{class:"field",style:"flex:1;min-width:200px"},h("label",{for:"f-title"},"Title"),title)),
      h("div",{class:"field"},h("label",{for:"f-file"},"Audio or text file (audio transcripts have no speakers, so you'll need to assign more owners yourself)"),file),
      h("div",{class:"field"},h("label",{for:"f-text"},"Or paste text"),text),
      btn,h("p",{class:"mute"},"Please make sure participants are aware before submitting. Text is sent to a model service for processing, and audio is deleted immediately after transcription.")));
}

function quoteBtn(text,uid,label,cls){
  return h("button",{class:"q "+(cls||""),title:"Jump to the transcript","data-testid":"quote",onclick:()=>highlight(uid)},
    label?h("small",{},label):null,`“${text}”`);
}
function highlight(uid){
  document.querySelectorAll(".u.hl").forEach(x=>x.classList.remove("hl"));
  const e=document.querySelector(`[data-uid="${CSS.escape(uid)}"]`);
  if(e){e.classList.add("hl");e.scrollIntoView({block:"center",behavior:"smooth"});}
  else toast("This quote is from an earlier meeting");
}
function fbButtons(token,type,id){
  const send=guard(async(rating,reason,comment)=>{await api(`/api/l/${token}/feedback`,{method:"POST",json:{target_type:type,target_id:String(id),rating,reason:reason||"",comment:comment||""}});toast("Feedback recorded");});
  const wrap=h("span",{class:"row",style:"gap:4px"});
  const up=h("button",{"aria-label":"This is right","data-testid":"fb-up",title:"This is right",onclick:()=>{send("up");wrap.replaceChildren(h("span",{class:"mute"},"Thanks"));}},"👍");
  const down=h("button",{"aria-label":"This is wrong","data-testid":"fb-down",title:"This is wrong",onclick:()=>{
    const sel=h("select",{"data-testid":"fb-reason","aria-label":"What's wrong"},["Wrong quote","Wrong owner","Wrong due date","Wrong status","Shouldn't be a task","Missing content","Other"].map(x=>h("option",{},x)));
    const c=h("input",{placeholder:"Details (optional)","data-testid":"fb-comment"});
    wrap.replaceChildren(sel,c,h("button",{"data-testid":"fb-send",onclick:()=>{send("down",sel.value,c.value);wrap.replaceChildren(h("span",{class:"mute"},"Recorded"));}},"Submit"));
  }},"👎");
  wrap.append(up,down);return wrap;
}

async function renderMeeting(body,r,led){
  const d=await api(`/api/l/${r.token}/meetings/${r.code}`);
  const m=d.meeting;
  body.replaceChildren();
  if(m.status==="processing"){
    const st=STAGE[m.stage]||["Processing",50];
    body.classList.add("narrow");
    body.append(h("h1",{},`${m.date} · ${m.title||KIND[m.kind]}`),h("div",{class:"card","data-testid":"processing"},h("div",{},st[0]+"…"),h("div",{class:"prog"},h("i",{style:`width:${st[1]}%`})),h("p",{class:"mute"},"Usually takes 1 to 3 minutes, longer for long meetings or recordings. You can leave this page and come back later.")));
    timer=setTimeout(render,2500);
    return;
  }
  if(m.status==="failed"){
    body.classList.add("narrow");
    body.append(h("h1",{},"This meeting couldn't be processed"),h("div",{class:"banner err","data-testid":"meeting-error"},m.error||"Unknown error"),h("button",{class:"primary",onclick:()=>go(`/l/${r.token}/new`)},"Submit again"));
    return;
  }
  const refresh=guard(async()=>{const y=window.scrollY;await render();window.scrollTo(0,y);});
  const left=h("div",{}),right=h("div",{class:"transcript","data-testid":"transcript"},h("h3",{style:"margin-top:0"},"Transcript"),
    d.utterances.map(u=>h("div",{class:"u","data-uid":u.id},u.ts?h("span",{class:"ts"},u.ts):null,u.speaker?h("span",{class:"sp"},u.speaker+": "):null,u.text)));
  body.append(h("div",{class:"row"},h("h1",{style:"flex:1"},`${m.date} · ${m.title||KIND[m.kind]}`),
    h("a",{href:`/api/l/${r.token}/export/${m.code}.md`,download:`${m.date}-minutes.md`,"data-testid":"export"},"Export minutes as Markdown")),
    h("div",{class:"split"},left,right));
  if(led.is_sample) left.append(h("div",{class:"banner","data-testid":"sample-guide"},"This is a fictional sample that replays the results of a real model run. Start with the first card: gray is what was said last time, green is what was said this time. If it's right, click “Confirm”, then check the task board to see what changed."));
  if(m.injections.length) left.append(h("div",{class:"banner","data-testid":"injection-banner"},`The meeting contained ${m.injections.length} passage(s) that look like instructions to an AI. They were treated as ordinary meeting content and not executed.`));
  if(m.rejected.length) left.append(h("details",{class:"banner","data-testid":"rejected-banner"},h("summary",{},`${m.rejected.length} model output(s) failed validation and were discarded. Click to see them`),m.rejected.map(x=>h("div",{class:"mute"},`${x.quote?`“${x.quote}”: `:""}${x.reason}`))));
  if(m.suspicious) left.append(h("div",{class:"banner err"},"The same sentence was used to close many items. Please review each one carefully."));

  const modelProps=d.proposals.filter(p=>p.proposed_by==="model");
  const nm=d.proposals.filter(p=>p.transition==="not_mentioned");
  if(d.proposals.length){
    left.append(h("h2",{"data-testid":"recon-title"},"What happened to last meeting's items"));
    const pending=modelProps.filter(p=>p.decision==="pending").length;
    left.append(h("p",{class:"mute"},pending?`${pending} still waiting for your confirmation. The task board changes only after you confirm.`:"Everything in this group has been handled."));
    for(const t of ["fulfilled","partial_or_rescheduled","abandoned"]){
      const ps=modelProps.filter(p=>p.transition===t);
      if(!ps.length) continue;
      left.append(h("h3",{},`${T[t]} (${ps.length})`),...ps.map(p=>propCard(p,r,refresh)));
    }
    if(nm.length){
      left.append(h("h3",{},`Not mentioned (${nm.length})`));
      for(const p of nm){
        const pm=(p.flags.find(f=>f.possible_mention)||{}).possible_mention;
        left.append(h("div",{class:"card","data-testid":"unmentioned"},
          h("div",{class:"row"},p.unmentioned>=2?h("span",{class:"badge b-bad"},`Not mentioned for ${p.unmentioned} meetings in a row`):h("span",{class:"badge"},"Not mentioned this meeting"),h("span",{class:"mute"},`${p.owner_value||"No owner"} · ${p.item_meeting||"Manual"}`)),
          h("div",{},p.item_title||`“${p.item_quote}”`),
          pm?h("div",{class:"banner"},"It may have come up, please take a look: ",quoteBtn(pm.text,pm.utterance_id)):null));
      }
    }
  }
  const drafts=d.items.filter(i=>i.kind==="commitment"&&i.review!=="merged");
  const merged=d.items.filter(i=>i.review==="merged");
  left.append(h("h2",{"data-testid":"drafts-title"},`New tasks from this meeting (${drafts.length})`));
  if(!drafts.length) left.append(h("p",{class:"mute"},"No tasks were extracted from this meeting."));
  drafts.forEach(i=>left.append(draftCard(i,r,led,refresh)));
  if(merged.length) left.append(h("p",{class:"mute","data-testid":"merged-note"},`${merged.length} more utterance(s) referred to last meeting's items. They were merged into the reconciliation above, so no duplicate tasks were created.`));
  for(const [k,tt] of [["decision","Decisions"],["result","Results"],["question","Open questions"]]){
    const xs=d.items.filter(i=>i.kind===k);
    if(xs.length) left.append(h("h2",{},`${tt} (${xs.length})`),...xs.map(i=>h("div",{class:"card","data-testid":"info-item"},i.title?h("strong",{},i.title):null,quoteBtn(i.quote,i.utterance_id),fbButtons(r.token,"item",i.id))));
  }
  const fu=await api(`/api/l/${r.token}/followup/${m.code}`);
  if(fu.text){
    left.append(h("h2",{},"Post-meeting follow-up"),h("pre",{class:"copy","data-testid":"followup"},fu.text),
      h("button",{"data-testid":"copy-followup",onclick:guard(async()=>{await navigator.clipboard.writeText(fu.text);toast("Copied");})},"Copy"));
  }
}
function propCard(p,r,refresh){
  const act=guard(async decision=>{await api(`/api/l/${r.token}/proposals/${p.id}/decide`,{method:"POST",json:{decision}});refresh();});
  const done=p.decision!=="pending";
  return h("div",{class:"card","data-testid":"proposal"},
    h("div",{class:"row"},h("span",{class:"badge "+(p.transition==="fulfilled"?"b-ok":p.transition==="abandoned"?"b-bad":"b-warn")},T[p.transition]),
      h("span",{class:"mute"},`${p.owner_value||"No owner"} · ${p.item_meeting||"Manual"}`),
      p.item_kind==="question"?h("span",{class:"badge"},"Open question"):null,
      p.new_due_raw?h("span",{class:"badge"},"New time: "+p.new_due_raw+(p.new_due_date?" → "+p.new_due_date:" (unclear time)")):null,
      p.flags.includes("multiple_items")?h("span",{class:"badge b-warn"},"May match multiple items"):null),
    p.item_title?h("strong",{},p.item_title):null,
    h("div",{class:"q"},h("small",{},`Then (${p.item_meeting_date||"added manually"})`),`“${p.item_quote||p.item_title}”`),
    p.evidence.map((e,n)=>quoteBtn(e.quote,e.utterance_id,n?"":"This time","closing")),
    h("div",{class:"row",style:"margin-top:6px"},
      done?h("span",{class:"badge "+(p.decision==="confirmed"?"b-ok":"")},p.decision==="confirmed"?"Confirmed":"Dismissed"):null,
      done?h("button",{"data-testid":"prop-undo",onclick:()=>act("pending")},"Undo"):h("button",{class:"primary","data-testid":"prop-confirm",onclick:()=>act("confirmed")},"Confirm"),
      done?null:retype(p,r,refresh),
      done?null:h("button",{"data-testid":"prop-dismiss",onclick:()=>act("dismissed")},"Wrong, dismiss"),
      h("span",{class:"spacer"}),fbButtons(r.token,"proposal",p.id)));
}
function retype(p,r,refresh){
  const others=Object.entries(T).filter(([k])=>k!==p.transition&&k!=="not_mentioned");
  const sel=h("select",{"data-testid":"prop-retype","aria-label":"Change to another status",onchange:guard(async()=>{
    if(!sel.value) return;
    await api(`/api/l/${r.token}/proposals/${p.id}/decide`,{method:"POST",json:{decision:"confirmed",transition:sel.value}});toast("Status changed and confirmed");refresh();})},
    h("option",{value:""},"Change to…"),others.map(([k,v])=>h("option",{value:k},v)));
  return sel;
}
function ownerField(i,r,led,onchange){
  const list="members-list";
  const inp=h("input",{value:i.owner_value&&i.owner_state==="given"?i.owner_value:"",placeholder:i.owner_state==="vague"?`Quote says “${i.owner_value||"unspecified"}”; assign to…`:"Unassigned",list,"data-testid":"owner","aria-label":"Owner",style:"width:150px",onchange:()=>onchange({owner:inp.value})});
  return h("span",{},inp,h("datalist",{id:list},led.members.map(x=>h("option",{value:x}))));
}
function draftCard(i,r,led,refresh){
  const patch=guard(async j=>{await api(`/api/l/${r.token}/items/${i.id}`,{method:"PATCH",json:j});toast("Saved");refresh();});
  const rev=guard(async action=>{await api(`/api/l/${r.token}/items/${i.id}/review`,{method:"POST",json:{action}});refresh();});
  const due=h("input",{type:"date",value:i.due_date||"","data-testid":"due","aria-label":"Due date",onchange:()=>patch({due_date:due.value})});
  return h("div",{class:"card","data-testid":"draft","data-review":i.review},
    h("div",{class:"row"},h("span",{class:"badge "+(i.strength==="committed"?"b-ok":"b-warn")},STR[i.strength]||i.strength),
      i.owner_state!=="given"?h("span",{class:"badge b-warn"},"Unassigned"):null,
      i.due_state==="vague"?h("span",{class:"badge b-warn"},"Unclear time: "+i.due_raw):null,
      i.review==="confirmed"?h("span",{class:"badge b-ok"},"On task board"):i.review==="rejected"?h("span",{class:"badge"},"Rejected"):null),
    i.title?h("strong",{"data-testid":"draft-title"},i.title):null,
    quoteBtn(i.quote,i.utterance_id,i.speaker?i.speaker+" said":"Quote"),
    h("div",{class:"row"},h("span",{class:"lbl"},"Owner"),ownerField(i,r,led,patch),h("span",{class:"lbl"},"Due date"),due,
      i.due_raw&&i.due_date?h("span",{class:"mute"},"Quote: "+i.due_raw):null),
    h("div",{class:"row",style:"margin-top:8px"},
      i.review==="pending"?[h("button",{class:"primary","data-testid":"draft-confirm",onclick:()=>rev("confirm")},"Confirm and add to task board"),h("button",{"data-testid":"draft-reject",onclick:()=>rev("reject")},"Not a task")]
        :h("button",{"data-testid":"draft-reopen",onclick:()=>rev("reopen")},"Undo"),
      h("span",{class:"spacer"}),fbButtons(r.token,"item",i.id)));
}

async function renderTasks(body,r,led){
  const {tasks}=await api(`/api/l/${r.token}/tasks`);
  body.replaceChildren();
  const who=new URLSearchParams(location.search).get("who")||"";
  const owners=[...new Set(tasks.map(t=>t.owner_value||""))].sort();
  const sel=h("select",{"data-testid":"filter-owner","aria-label":"Filter by owner",onchange:()=>go(`/l/${r.token}/tasks${sel.value?"?who="+encodeURIComponent(sel.value):""}`)},
    h("option",{value:""},"Everyone"),owners.filter(Boolean).map(o=>h("option",{value:o,selected:o===who},o)));
  const title=h("input",{placeholder:"Add a task manually","data-testid":"new-task-title",style:"flex:1;min-width:180px","aria-label":"Task description"});
  const owner=h("input",{placeholder:"Owner",list:"mlist","data-testid":"new-task-owner",style:"width:120px","aria-label":"Owner"});
  const due=h("input",{type:"date","data-testid":"new-task-due","aria-label":"Due date"});
  const add=guard(async()=>{if(!title.value.trim())return toast("Enter a task description");await api(`/api/l/${r.token}/tasks`,{method:"POST",json:{title:title.value,owner:owner.value||null,due_date:due.value||null}});render();});
  const open=tasks.filter(t=>["todo","doing"].includes(t.task_status));
  const people=[...new Set(open.map(t=>t.owner_state==="given"&&t.owner_value?t.owner_value:"Unassigned"))];
  const tdy=today();
  const summary=h("div",{class:"row","data-testid":"owner-summary",style:"margin:8px 0"},people.map(p=>{
    const mine=open.filter(t=>(t.owner_state==="given"&&t.owner_value?t.owner_value:"Unassigned")===p);
    const late=mine.filter(t=>t.due_date&&t.due_date<tdy).length;
    return h("span",{class:"badge "+(late?"b-bad":"")},`${p}: ${mine.length} open${late?`, ${late} overdue`:""}`);}));
  body.append(h("div",{class:"row"},h("h1",{style:"flex:1"},"Task board"),h("a",{href:`/api/l/${r.token}/tasks.csv`,"data-testid":"export-csv"},"Export CSV"),sel),summary,
    h("div",{class:"card row"},title,owner,h("datalist",{id:"mlist"},led.members.map(x=>h("option",{value:x}))),due,h("button",{"data-testid":"new-task-add",onclick:add},"Add")));
  if(!tasks.length) body.append(h("p",{class:"mute","data-testid":"board-empty"},"No tasks yet. Draft tasks appear here after you confirm them on a meeting page."));
  const shown=tasks.filter(t=>!who||t.owner_value===who);
  const td=today();
  body.append(h("div",{class:"board"},COLS.map(([k,name])=>h("div",{class:"col","data-testid":"col-"+k},h("h3",{},`${name} (${shown.filter(t=>t.task_status===k).length})`),
    shown.filter(t=>t.task_status===k).map(t=>taskCard(t,r,led,td))))));
}
function taskCard(t,r,led,td){
  const patch=guard(async j=>{await api(`/api/l/${r.token}/items/${t.id}`,{method:"PATCH",json:j});render();});
  const status=guard(async task_status=>{await api(`/api/l/${r.token}/items/${t.id}/status`,{method:"POST",json:{task_status}});render();});
  const overdue=t.due_date&&t.due_date<td&&["todo","doing"].includes(t.task_status);
  const owner=h("input",{value:t.owner_state==="given"?t.owner_value||"":"",placeholder:"Unassigned",list:"mlist","data-testid":"task-owner","aria-label":"Owner",style:"width:110px",onchange:()=>patch({owner:owner.value})});
  const due=h("input",{type:"date",value:t.due_date||"","data-testid":"task-due","aria-label":"Due date",onchange:()=>patch({due_date:due.value})});
  const st=h("select",{"data-testid":"task-status","aria-label":"Status",onchange:()=>status(st.value)},COLS.map(([k,n])=>h("option",{value:k,selected:k===t.task_status},n)));
  return h("div",{class:"task"+(overdue?" overdue":""),"data-testid":"task"},
    h("div",{},t.title||`“${t.quote}”`),
    t.title&&t.quote?h("div",{class:"mute"},`“${t.quote}”`):null,
    t.meeting_id?h("div",{class:"mute"},link(`/l/${r.token}/m/${t.m_code}`,`From ${t.m_date}`)):h("div",{class:"mute"},"Added manually"),
    overdue?h("span",{class:"badge b-bad"},"Overdue"):null,
    t.unmentioned>=2?h("span",{class:"badge b-bad"},`Not mentioned for ${t.unmentioned} meetings in a row`):null,
    h("div",{class:"row",style:"margin-top:6px"},owner,due,st));
}

function renderSettings(body,r,led){
  body.classList.add("narrow");
  const mem=h("textarea",{value:led.members.join("\n"),style:"min-height:120px","data-testid":"members","aria-label":"Member list"});
  const terms=h("textarea",{value:(led.terms||[]).join("\n"),style:"min-height:90px","data-testid":"terms","aria-label":"Glossary"});
  const save=guard(async()=>{await api(`/api/l/${r.token}/members`,{method:"POST",json:{members:mem.value.split(/[\n,，、]/),terms:terms.value.split(/[\n,，、]/)}});toast("Saved");render();});
  const del=guard(async()=>{
    if(!confirm("Permanently delete all meetings, transcripts, tasks and feedback in this ledger? This can't be undone.")) return;
    await api(`/api/l/${r.token}`,{method:"DELETE"});go("/");
  });
  body.append(h("h1",{},"Settings"),
    h("h2",{},"Share link"),h("div",{class:"card"},h("p",{class:"mute"},"Anyone with this link can view and edit this ledger."),h("code",{"data-testid":"share-link",style:"word-break:break-all;display:block;margin-bottom:8px"},`${location.origin}/l/${r.token}`),h("button",{"data-testid":"copy-link",onclick:guard(async()=>{await navigator.clipboard.writeText(`${location.origin}/l/${r.token}`);toast("Link copied");})},"Copy link")),
    h("h2",{},"Member list"),h("div",{class:"card"},h("p",{class:"mute"},"One per line. Used to standardize owner names and provide assignment options."),mem,h("h3",{},"Glossary"),h("p",{class:"mute"},"One per line, e.g. baseline, LoRA. Helps speech transcription get technical terms right."),terms,h("button",{"data-testid":"save-members",onclick:save,style:"margin-top:8px"},"Save")),
    h("h2",{},"Delete"),h("div",{class:"card"},h("button",{class:"danger","data-testid":"delete-ledger",onclick:del},"Permanently delete this ledger")));
}

function openSurvey(token){
  const close=()=>m.remove();
  const se=[["very","Very disappointed"],["somewhat","Somewhat disappointed"],["not","Not disappointed"]];
  let pick=null;
  const opts=h("div",{class:"row"},se.map(([k,t])=>{const b=h("button",{"data-testid":"se-"+k,onclick:()=>{pick=k;opts.querySelectorAll("button").forEach(x=>x.classList.remove("primary"));b.classList.add("primary");}},t);return b;}));
  const v=h("textarea",{style:"min-height:70px","data-testid":"survey-value","aria-label":"What's most useful"});
  const miss=h("textarea",{style:"min-height:70px","data-testid":"survey-missing","aria-label":"What's missing or not working well"});
  const send=guard(async()=>{if(!pick)return toast("Please choose one");await api(`/api/l/${token}/survey`,{method:"POST",json:{sean_ellis:pick,value_text:v.value,missing:miss.value}});close();toast("Got it, thanks");});
  const m=h("div",{class:"modal",role:"dialog","aria-modal":"true"},h("div",{},h("h2",{style:"margin-top:0"},"Your feedback"),
    h("p",{},"How disappointed would you be if you could no longer use this product starting tomorrow?"),opts,
    h("p",{},"What's most useful about it for you?"),v,h("p",{},"What's missing, or what doesn't work well?"),miss,
    h("div",{class:"row",style:"margin-top:10px"},h("button",{class:"primary","data-testid":"survey-send",onclick:send},"Submit"),h("button",{onclick:close},"Cancel"))));
  document.body.append(m);
}
render();
