n_tabs = int(input())
salary = int(input())

facebook_tabs = 0
instagram_tabs = 0
reddit_tabs = 0

for n in range(1, n_tabs + 1):
    website_name = input()
    if website_name == "Facebook":
        facebook_tabs = facebook_tabs + 1
    elif website_name == "Instagram":
        instagram_tabs = instagram_tabs + 1
    elif website_name == "Reddit":
        reddit_tabs = reddit_tabs + 1
    penalty_facebook = 150 * facebook_tabs
    penalty_instagram = 100 * instagram_tabs
    penalty_reddit = 50 * reddit_tabs

    total_penalty = penalty_facebook + penalty_instagram + penalty_reddit
    diff = salary - total_penalty

    if total_penalty >= salary:
        print("You have lost your salary.")
        break
if total_penalty < salary:
    print(diff)

