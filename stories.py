"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

stories = {'story1':'Way back in {place}, there lived a silly {adjective} {noun}. It would always {verb} {plural_noun}.', 'story2':'Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.', 'story3':"In west {place}, there resided a chill {adjective} {noun}. It never didn't {verb} {plural_noun}."}
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    stories['story1']
)


story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    stories['story2']
)

story3 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    stories['story3']
)

stories = {'story1':story, 'story2':story2, 'story3':story3}