import hashlib, os, time

USERS = {"pankaj_singh": "my_super_secret_password"}

class Server:
    def __init__(self):
        self.challenges = {}

    def gen_challenge(self, user):
        if user not in USERS: return None, "User not found"
        ch = os.urandom(8).hex() + "_" + str(int(time.time()))
        self.challenges[user] = (ch, time.time() + 60)
        print(f"Server: Challenge for {user}: {ch[:10]}...")
        return ch, None

    def verify(self, user, challenge, resp):
        if user not in self.challenges: return False, "No challenge"
        ch, exp = self.challenges[user]
        if ch != challenge or time.time() > exp: return False, "Expired or invalid"
        ok = hashlib.sha256((ch + USERS[user]).encode()).hexdigest() == resp
        del self.challenges[user]
        return (ok, "Success" if ok else "Fail")

class Client:
    def __init__(self, user, pwd): self.user, self.pwd = user, pwd
    def respond(self, ch): return hashlib.sha256((ch + self.pwd).encode()).hexdigest()

if __name__ == "__main__":
    srv = Server()
    cli = Client("pankaj_singh", "my_super_secret_password")

    print("\n--- Successful Login ---")
    ch, _ = srv.gen_challenge(cli.user)
    resp = cli.respond(ch)
    print("Client Response:", resp[:10], "...")
    print("Server:", srv.verify(cli.user, ch, resp)[1])

    print("\n--- Replay Attack ---")
    old_resp = resp
    ch2, _ = srv.gen_challenge(cli.user)
    print("Attacker replays old response...")
    print("Server:", srv.verify(cli.user, ch2, old_resp)[1])
