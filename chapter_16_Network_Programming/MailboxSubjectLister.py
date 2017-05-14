import email
import mailbox
import sys

if len(sys.argv) < 2:
    print("Usage : %s [path to mailbox file]" % sys.argv[0])
    sys.exit([1])

path = sys.argv[1]
fp = open(path, 'rb')
subjects = []

for message in mailbox.PortableUnixMailBox(fp, email.message_from_file):
    subjects.append(message["subject"])

print("'s message(s) in mailbox %s : " % (len(subjects, path)))
for subject in subjects:
    print('', subject)