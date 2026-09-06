class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for email in emails:
            local, domain = email.split("@")

            if "+" in local:
                local = local[:local.index("+")]

            local = local.replace(".", "")

            s.add(local + "@" + domain)

        return len(s)