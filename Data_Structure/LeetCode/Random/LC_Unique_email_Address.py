# https://leetcode.com/problems/unique-email-addresses/

# Every valid email consists of a local name and a domain name, separated by the '@' sign.
# Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address,
# mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:

        self.unique_emails = set ()  # create a unique set
        # loop through email list
        for email in emails:
            # capture name & domain seperately using @ seperator
            name = email[ : email.find('@')+1 ]
            domain =  email[ email.find('@') : ]

            #replace . with blank
            name = name.replace('.','')
            # find index postion of + and read element from start index to only until + sign index
            name= name[:name.find('+')]

            # join both of them toghether
            full_email = name + domain
            # add in Unique set
            self.unique_emails.add(full_email)

        # return the set
        return len(self.unique_emails)

def main():

    s = Solution()
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print("Number of Unique email IDs are " , s.numUniqueEmails(emails))

if __name__ == "__main__":
    main()