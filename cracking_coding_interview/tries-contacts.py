def address_book():
    n = int(raw_input().strip())
    contacts = set([])
    for a0 in xrange(n):
        op, contact = raw_input().strip().split(' ')
        if op == "add":
            contacts.add(contact)
            print contacts
        elif op == "find":
            count = 0
            for person in contacts:
                print person.find(contact)
                if person.find(contact) > -1:
                    count += 1
            print count

address_book()
