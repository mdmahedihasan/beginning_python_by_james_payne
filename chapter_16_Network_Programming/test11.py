from imaplib import IMAP4


class SubjectLister(IMAP4):
    def __init__(self, server, username, password):
        IMAP4.__init__(self, server)
        self.debug = 4
        self.login(username, password)

    def summarize(self, mailbox="Inbox"):
        numberOfMessages = int(self._result(self.select(mailbox)))
        print("%s message(s) in mailbox %s : " % (numberOfMessages, mailbox))
        subjects = self._result(self.fetch("1 : %d" % numberOfMessages, '(BODY[HEADER.FIELDS(SUBJECT)])'))

        for subject in subjects:
            if hasattr(subject, '__iter__'):
                subject = subject[1]
                print('', subject[:subject.find('\n')])

    def _result(self, result):
        status, result = result
        if status != "OK":
            raise status(result)
        if len(result) == 1:
            result = result[0]
        return result


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4:
        print("usage : %s [IMAP hostname] [IMAP user] [IMAP password]" % sys.argv[0])
        sys.exit(0)

    lister = SubjectLister(sys.argv[1], sys.argv[2], sys.argv[3])
    lister.summarize()