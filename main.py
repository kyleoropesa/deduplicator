import utils

if __name__ == '__main__':
    cycles = 20
    for _ in range(cycles):
        emails = utils.create_list_of_unique_and_duplicate_emails(size=100000, duplicate_percent=.5)
        # print(emails)
        utils.deduplicate_list(emails)
        # print(utils.deduplicate_list(emails))
