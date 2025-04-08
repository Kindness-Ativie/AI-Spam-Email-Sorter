# Assignment 3 Kindness Ativie
from tabulate import tabulate
import numpy


# 6. Consider a "test email" * * *

test_email = str(input("✨📧 Please enter an email into the spam ham calculator ---->: "))

# 1. Start with 10 emails, mix of spam and ham emails. * * *

email_1 = "Please pay your bill urgently. Send license, credit card info, address, and SSN to pay."  # spam
email_2 = "Congratulations! You have won a free MacBook Air! Reply with your address and contact info."  # spam
email_3 = "Thank you for payment to Cardinal Central. Your pay: $1,500. - The Financial Aid Office."  # ham
email_4 = "Grandma, Billy is in Urgent Care with a concussion. The doctors say he has a 20% chance of recovery."  # ham
email_5 = "You are being hacked! Contact UltraSupport! Urgent! Call this number: 555-892-9995."  # spam
email_6 = "We received your application for the JPMorganChase finance internship. Track your application here: "  # ham
email_7 = "Hello Bob. Submit the Excel file with the updated financial documents by end of day. - Your boss"  # ham
email_8 = "Hello Microsoft staff. Due to the 70% chance of rain, we are canceling the outdoor brunch. - HR "  # ham
email_9 = "Your bank account has been hacked. Send us your password to recover your information for free."  # spam
email_10 = "Welcome to the team. You will need your SSN, license, and credit card for onboarding paperwork."  # ham

# 2. Convert to lower case. * * *

# creation of lists for original emails
all_emails = [email_1, email_2, email_3, email_4, email_5, email_6, email_7, email_8, email_9, email_10]
ham_emails = [email_3, email_4, email_6, email_7, email_8, email_10]
spam_emails = [email_1, email_2, email_5, email_9]

# emails converted to lowercase
lower_all_emails = []
for email in all_emails:
    lower_email = email.lower()
    lower_all_emails.append(lower_email)


# allows user to display all emails
def display_all_emails():
    for email in all_emails:
        print(email, "\n")


# allows user to display all emails in lowercase form
def display_lower_case_emails():
    for email in lower_all_emails:
        print(email, "\n")


# 3. Remove stop words. * * *

stop_words = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no",
              "not", "of", "on", "or", "such", "that", "the", "their", "then", "these", "they", "this", "to", "was",
              "will", "with", "you", "they", "them", "this", "there", "your", "has", "in", "for", "we", "he", "she",
              "been", "us", "need", "being", "have", "hi", "hello", "say", "said", "saying", "welcome", "please",
              "thank", "thanks"]

email_1_words = email_1.split()
result_words = [word for word in email_1_words if word not in stop_words]
result = ' '.join(result_words)

no_stop_words = []

for email in lower_all_emails:
    email_words = email.split()
    result_words_2 = [word for word in email_words if word not in stop_words]
    result_2 = ' '.join(result_words_2)
    no_stop_words.append(result_2)


def show_without_stop_words():
    for sentence in no_stop_words:
        print(sentence, "\n")


# 4. Remove special characters. * * *

special_characters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}",
                      "[", "]", "|", "/", "?", ",", ".", ":"]

cleaned_email = []
for email in no_stop_words:
    result_words_3 = ''.join(letter for letter in email if letter not in special_characters)
    cleaned_email.append(result_words_3)


# allows user to display without special characters and stop words
def show_without_special_characters():
    for email in cleaned_email:
        print(email, "\n")


# 5. Create a vocabulary of all the unique words with their occurrence in spam vs. ham.
total_words = []  # stores total words in all 10 emails

for line in cleaned_email:
    word = line.split()
    for item in word:
        total_words.append(item)


# allows user to see total words and its count
def display_total_words():
    print(f"Total words: {len(total_words)}")  # counts total words in all 10 emails


unique_words = set(total_words)  # finds unique words by removing duplicates using set
total_unique_words = len(unique_words)  # counts the length of unique words


# allows user to see all unique words and their count
def display_total_unique_words():
    print(f"Total unique words: {total_unique_words}")


# lowers and cleans special characters from list of all spam emails
all_spam_email_words = []
for email in spam_emails:
    item = email.split()
    for x in item:
        all_spam_email_words.append(x)

lower_all_spam_email_words = ([x.lower() for x in all_spam_email_words])

cleaned_all_spam_email_words = []
for email in lower_all_spam_email_words:
    result_words_4 = ''.join(letter for letter in email if letter not in special_characters)
    cleaned_all_spam_email_words.append(result_words_4)


# lowers and cleans special characters from list of all ham emails
all_ham_email_words = []
for email in ham_emails:
    item = email.split()
    for x in item:
        all_ham_email_words.append(x)

lower_all_ham_email_words = ([x.lower() for x in all_ham_email_words])

cleaned_all_ham_email_words = []
for email in lower_all_ham_email_words:
    result_words_5 = ''.join(letter for letter in email if letter not in special_characters)
    cleaned_all_ham_email_words.append(result_words_5)


# creates table formatting
table_spam_ham_1 = [["WORD", "SPAM", "HAM"]]
for word in unique_words:
    table_row = []
    a = cleaned_all_spam_email_words.count(word)
    b = cleaned_all_ham_email_words.count(word)
    table_row.append(word)
    table_row.append(a)
    table_row.append(b)
    table_spam_ham_1.append(table_row)


# allows user to see spam ham composition of words
def show_spam_ham_composition():
    print(tabulate(table_spam_ham_1, tablefmt="simple_grid"))


# 7. Perform cleanup à lowercase, removal of stop words, special characters, and new words

all_test_email_words = []
item = test_email.split()
for x in item:
    all_test_email_words.append(x)

lower_all_test_email_words = ([x.lower() for x in all_test_email_words])

cleaned_all_test_email_words = []
for email in lower_all_test_email_words:
    result_words_6 = ''.join(letter for letter in email if letter not in special_characters)
    cleaned_all_test_email_words.append(result_words_6)

no_new_words = []
# note: because unique words automatically excludes stop words no need to remove stop words first. Avoids redundancy.
result_words_7 = [word for word in cleaned_all_test_email_words if word in unique_words]

result_7 = ' '.join(result_words_7)
no_new_words.append(result_7)


def show_purified_test_email():
    before_after_table = [["ORIGINAL EMAIL", "PURIFIED EMAIL"], [test_email, ''.join(no_new_words)]]
    print(tabulate(before_after_table, tablefmt="fancy_grid"))


# 8. Using Laplace smoothing calculate the probability of being spam. * * *

separated_purified_test = []

for l in no_new_words:
    separated_purified_test = (l.split())

Pspam = len(spam_emails) / len(all_emails)

table_all_probs_of_spam = [["P(word)|spam", "="]]
all_probs_of_spam = []
for word in separated_purified_test:
    a = cleaned_all_spam_email_words.count(word)
    Pwi = (a + 1) / ((len(spam_emails)) + total_unique_words)
    all_probs_of_spam.append(Pwi)
    spam_word_prob = []
    spam_word_prob.append(f"P({word})|spam")
    spam_word_prob.append(Pwi)
    table_all_probs_of_spam.append(spam_word_prob)
table_all_probs_of_spam.append(["P(Spam)", Pspam])


# allows user to see table of spam probabilities
def show_me_spam_table_probabilities():
    print(tabulate(table_all_probs_of_spam, tablefmt="double_grid"))

    probability_of_spam = (numpy.prod(all_probs_of_spam)) * Pspam
    print("PROBABILITY OF SPAM Pre-Normalization: ", probability_of_spam)
    print("Normalization factor: ", normalization_factor)


# P(wi) = (count(wi) + 1) / (total words + unique words)
# 9. Using Laplace smoothing calculate the probability of being ham.
Pham = len(ham_emails) / len(all_emails)

separated_purified_test_2 = []

for l in no_new_words:
    separated_purified_test_2 = (l.split())

table_all_probs_of_ham = [["P(word)|ham", "="]]
all_probs_of_ham = []
for word in separated_purified_test_2:
    b = cleaned_all_ham_email_words.count(word)
    Pwi_h = (b + 1) / ((len(ham_emails)) + total_unique_words)
    all_probs_of_ham.append(Pwi_h)
    ham_word_prob = []
    ham_word_prob.append(f"P({word})|ham")
    ham_word_prob.append(Pwi_h)
    table_all_probs_of_ham.append(ham_word_prob)
table_all_probs_of_ham.append(["P(Ham)", Pham])


# allows user to see table of ham probabilities
def show_me_ham_table_probabilities():
    print(tabulate(table_all_probs_of_ham, tablefmt="double_grid"))

    probability_of_ham = (numpy.prod(all_probs_of_ham)) * Pham
    print("PROBABILITY OF HAM Pre-Normalization: ", probability_of_ham)
    print("Normalization factor: ", normalization_factor)


# 10. There isn’t any right or wrong answer but make sure adding the both probability is ≈ 1 (or 100%)
probability_of_spam = (numpy.prod(all_probs_of_spam)) * Pspam
probability_of_ham = (numpy.prod(all_probs_of_ham)) * Pham
normalization_factor = probability_of_spam + probability_of_ham


normalized_spam_prob = probability_of_spam / normalization_factor
normalized_ham_prob = probability_of_ham / normalization_factor


def show_final_analysis():
    print("SPAM VS. HAM Analysis")
    final_analysis_table = [["Normalization factor:", normalization_factor],
                            [f"P(spam| {''.join(no_new_words)})", "{:.0%}".format(normalized_spam_prob)],
                            [f"P(ham| {''.join(no_new_words)}", "{:.0%}".format(normalized_ham_prob)]]

    print(tabulate(final_analysis_table, tablefmt="mixed_grid"))

    if normalized_spam_prob > normalized_ham_prob:
        print("This email is most likely spam! :( ")
    elif normalized_spam_prob < normalized_ham_prob:
        print("This email is most likely ham. :)")
    else:
        print("There is a 50/50 chance of this email being spam or ham.")


# menu to navigate entire program

def menu():
    print("-" * 30)
    print("SPAM vs. HAM email detector 👀✉️")
    print("""
Option 1 = Display original 10 default emails
Option 2 = Display cleaned 10 default emails 🫧🧽
Option 3 = Display # of total words and total unique words
Option 4 = Display spam, ham, count table of 10 emails
Option 5 = Show test email before and after cleanse 🧼
Option 6 = Show me spam table probabilities 🧮
Option 7 = Show me ham table probabilities ✖️🟰

Option 8 = ** Highly Recommended ** Show final analysis: Is it spam or ham? 📈👀
Option 0 = Quit! 👋    
""")


def user_menu():
    menu()
    option = int(input("Please select option # ---->: "))
    if option != 0:
        match option:
            case 1:
                display_all_emails()
            case 2:
                show_without_special_characters()
            case 3:
                display_total_words()
                display_total_unique_words()
            case 4:
                show_spam_ham_composition()
            case 5:
                show_purified_test_email()
            case 6:
                show_me_spam_table_probabilities()
            case 7:
                show_me_ham_table_probabilities()
            case 8:
                show_final_analysis()
            case _:
                print("This option is not available. But there are others!")
        user_menu()

    else:
        print("Bye!")


user_menu()
