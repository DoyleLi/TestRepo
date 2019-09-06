from config import safe

BUILDBOT_TITLE = "LLVM SYCL CI"
BUILDBOT_TITLE_URL = "https://github.com/DoyleLi/llvm"
BUILDBOT_URL = "http://ec2-52-15-192-79.us-east-2.compute.amazonaws.com:8011/"
BUILDBOT_PROTOCOL_PORT = 9990
BUILDBOT_WEB_PORT = 8011
#BUILDBOT_DB = "sqlite:///state.sqlite"
BUILDBOT_DB = f"postgresql://buildbot:{safe.DB_P}@localhost/llvm_ci_otcshare"

# repo info
SOURCE_NAME="llvm-git-monorepo"
SOURCE_REPO="git@github.com:DoyleLi/llvm.git"
SOURCE_PROJECT="DoyleLi/llvm"

# github auth
GITHUB_ADMIN_GROUP_PREFIX="otcshare/"
GITHUB_ADMIN_GROUP="llvm-write"

# Branch to build
LLORG_BRANCH="master"
INTEL_BRANCH="intel"
SYCL_BRANCH="sycl"
CODEPLAY_BRANCH="codeplay"

# Worker running command
WORKER_COMMAND = "python3"

#misc
WAIT_PR_BRANCH_TIMEOUT=2*60*60
LOG_ENVIRON=False
