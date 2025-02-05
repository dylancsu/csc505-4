
class Engineer:
    def __init__(self, assertion, collab, technical):
        self.assertion = assertion
        self.collab=collab
        self.technical=technical
        print(f"Step 1. Engineer created with assertion: {assertion}, collab: {collab}, and technical: {technical}")
class SWE:
    def __init__(self,engineer, name):
        self.name=name
        self.engineer=engineer
        print(f"Step 2. Software Engineer {self.name} created with assertion: {engineer.assertion}, collab: {engineer.collab}, and technical: {engineer.technical}")

for e in ["Eric Raymond", "Linus Torvalds", "John Carmack"]:
    engineer = SWE(Engineer(True, True, True), e)
    print(f"Step 3. {e} created as SWE with assertion: {engineer.engineer.assertion}, collab: {engineer.engineer.collab}, and technical: {engineer.engineer.technical}")