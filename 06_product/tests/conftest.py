import os
import tempfile

os.environ["BP_DB"] = os.path.join(tempfile.mkdtemp(), "t.db")
os.environ["BP_PROVIDER"] = "none"
os.environ["BP_ADMIN_KEY"] = "k"
