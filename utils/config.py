import os
import environs

try:
    env = environs.Env()
    env.read_env("./.env")
except FileNotFoundError:
    print("No .env file found, using os.environ.")

api_id = int(os.getenv("API_ID", env.int("API_ID", "16885568")))
api_hash = os.getenv("API_HASH", env.str("API_HASH", "bd5a232cf132961aaac66da7d12b343c"))

STRINGSESSION = os.getenv("STRINGSESSION", env.str("STRINGSESSION", "BAC86fAAdBiRjmKjn1vLcUY7KqR6t-CZQ2WefK3hngxnIWLDnGxzUUjvxc2HaQkEXUmSqKWknASOsiVfLY6uNZOxv2ZKwdDp2voolhaODHLDihH-SiFsvRnQH1RHb6NPgVS2cj9QRZXVE_nExuIoHMNunkZTmK5FWt8HYtWu1buEvbNRqHV3YBAmGF1uzRWkkqh9Gtf9BfAtKvKZL9rslnqpCh1Hi1Y3o-4DM_V6gv9PXdF8lSw7NUVsUuZyhseA7-4LTlqh4ggxoZoxh73BrhuhQ7mVQJGNN2D777Xom3_xL2SSNsgMgXJG0toUr12UdDb3wrdNylh8zFCmhAJ7TogMSZn_6AAAAAEw7LtJAA"))

second_session = os.getenv("SECOND_SESSION", env.str("SECOND_SESSION", "BAC86fAAoSq8W__gERQRHxN_Ppq5ltRxpdqwHn3JAFX_Qq-E_CC_inh3rhnAaFlEborRQZhIIGS_GJbQrpdNXATKrryK9_7aqlY5N_aoZ14W0t93gxE4fp3mITA4dn6ejPLrtqxk8Mtr8iMDngfKktHxDyrlhsEvYUy_TaR-RmO-1Qeqx_Z9ie3dcOmn2hSZwFfBcdPBRvTsppDNBKYFhV46-YfKRv2WmbRb34tyw3mkh6WmLbrbynBpWu31xNSeifbM5iD5b2GeqIHVts5tg3EepT89UL0SpGkvbxu67pvDdRa5BTr3VamS6ZajNcmT8yWRXTE1ZatHy4UK0gIArpx-CyxUDAAAAAHwsneSAA"))

db_type = os.getenv("DATABASE_TYPE", env.str("DATABASE_TYPE"))
db_url = os.getenv("DATABASE_URL", env.str("DATABASE_URL", "mongodb+srv://omicron:omicron@cluster0.gs32lsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
db_name = os.getenv("DATABASE_NAME", env.str("DATABASE_NAME"))

apiflash_key = os.getenv("APIFLASH_KEY", env.str("APIFLASH_KEY", "https://api.apiflash.com/v1/urltoimage?access_key=96762a3d4d294cefab66606aaa7901f9&wait_until=page_loaded&url=http://google.com"))
rmbg_key = os.getenv("RMBG_KEY", env.str("RMBG_KEY", "MSTxovqQSwCboZYJiPaZKC1u"))
vt_key = os.getenv("VT_KEY", env.str("VT_KEY", "65bc241867f7f7354882f4b43fc4f10d2a8eaecd5d87540c11b4aa5f0057f09b"))
gemini_key = os.getenv("GEMINI_KEY", env.str("GEMINI_KEY", "AIzaSyDL3ao0YqnOqN73kNnpdDHNstt5iNvWq9A"))
cohere_key = os.getenv("COHERE_KEY", env.str("COHERE_KEY", "xgBXLD495HSVbEb2YguhjV1VG42qmaXbdFk4XVvr"))

pm_limit = int(os.getenv("PM_LIMIT", env.int("PM_LIMIT", 4)))

test_server = bool(os.getenv("TEST_SERVER", env.bool("TEST_SERVER", False)))
modules_repo_branch = os.getenv(
    "MODULES_REPO_BRANCH", env.str("MODULES_REPO_BRANCH", "master")
)
