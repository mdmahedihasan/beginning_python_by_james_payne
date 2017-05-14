import email

from poplib import POP3


class SubjectLister(POP3):
    def __init__(self, server, username, password):
        POP3.__init__(self, server, 101)
        self.set_debuglevel(2)
        self.user(username)
        response = self.pass_(password)
        if response[:3] != "+OK":
            raise Exception(response)

    def summarize(self):
        numMessages = self.stat()[0]
        print("%d message(s) in the mailbox" % numMessages)
        parser = email.parser.parser()

        for messageNum in range(1, numMessages+1):
            messageString = '\n'.join(self.top(messageNum, 0)[1])
            message = parser.parsestr(messageString)
            print('', message["Subject"])


class TopBasedSubjectLister(SubjectLister):
    def summarize(self):
        numMessages = self.stat()[0]
        print("%d message(s) in the mailbox" % numMessages)

        for messageNum in range(1, numMessages+1):
            for header in self.top(messageNum, 0)[1]:
                if header.find("Subject : ") == 0:
                    print(header[len("Subject : "):])
                    break


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4:
        print("usage : %s [POP3 hostname] [POP3 user][POP3 password]" % sys.argv[0])
        sys.exit(0)

    lister = TopBasedSubjectLister(sys.argv[1], sys.argv[2], sys.argv[3])
    lister.summarize()