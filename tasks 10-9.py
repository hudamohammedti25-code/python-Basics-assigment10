def validate_tweet(input_text):
    if len(input_text) <= 140:
        return input_text
    else:
        return input_text[:140] + "..."

short_tweet = "Learning programming is very fun and easy with continuous practice!"
print("First tweet:")
print(validate_tweet(short_tweet))

print("-" * 30)
long_text = "This text is extremely, extremely long" * 10

print("The second tweet after examination and editing:")
print(validate_tweet(long_text))