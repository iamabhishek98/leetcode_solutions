class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        
        for email in emails:
            local, domain = email.split("@")
            actual = local.split("+")[0].replace('.','') + "@" + domain
            unique.add(actual)
        
        return len(unique)