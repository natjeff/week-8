
# Exercise 1:
from collections import defaultdict

class MarkovText:
    """
    Markov chain text generator class
    """

    def __init__(self, corpus):
        """
        Initialize the MarkovText object with a corpus
        """
        self.corpus = corpus
        self.term_dict = None

    def get_term_dict(self):
        """
        Build a transition dictionary from the corpus
        """
        # Split the corpus into tokens (words)
        tokens = self.corpus.split()
        term_dict = defaultdict(list)
        
        # Loop through all tokens except the last one
        for i in range(len(tokens) - 1):
            current_token = tokens[i]
            next_token = tokens[i + 1]
            term_dict[current_token].append(next_token)
        
        # Convert defaultdict to a regular dict for easier use and readability
        self.term_dict = dict(term_dict)
        return self.term_dict


# Example usage
text_gen = MarkovText(corpus)
print(text_gen.get_term_dict())

       




# Exercise 2:
import random

class MarkovText:
    """
    Markov chain text generator class
    """

    def __init__(self, corpus):
        """
        Initialize the MarkovText object with a corpus again
        """
        self.corpus = corpus
        self.term_dict = None

    def get_term_dict(self):
        """
        Build a transition dictionary again
        """
        tokens = self.corpus.split()
        term_dict = defaultdict(list)
        
        for i in range(len(tokens) - 1):
            current_token = tokens[i]
            next_token = tokens[i + 1]
            term_dict[current_token].append(next_token)
        
        self.term_dict = dict(term_dict)
        return self.term_dict

    def generate(self, term_count, seed_term=None):
        """
        Generate text using the Markov chain property. 
        It returns a string and raises a value error if the seed term is not found in the corpus.
        """
        # term dictionary building check
        if self.term_dict is None:
            self.get_term_dict()

        # Choose a starting term and raise value error if neccessary
        if seed_term:
            if seed_term not in self.term_dict:
                raise ValueError(f"'{seed_term}' not found in corpus.")
            current_term = seed_term
        else:
            current_term = random.choice(list(self.term_dict.keys()))

        # Initialize the generated sequence
        generated = [current_term]

        # Generate text using the Markov property
        for _ in range(term_count - 1):
            next_terms = self.term_dict.get(current_term)
            if not next_terms:
                # If we reach a term with no next tokens, pick a new random start
                current_term = random.choice(list(self.term_dict.keys()))
                generated.append(current_term)
                continue
            current_term = np.random.choice(next_terms)
            generated.append(current_term)

        return " ".join(generated)


# Example usage
text_gen = MarkovText(corpus)
text_gen.get_term_dict()

# Generate 10 terms, starting with "Healing"
print(text_gen.generate(term_count=10, seed_term="Healing"))

# Or let it pick a random start
print(text_gen.generate(term_count=10))
