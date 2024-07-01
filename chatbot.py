import re
import random


class RuleBot:
  ###potential Negetive Responses
  negetive_responses = ("no","nope","nah","naw","not a chance","sorry")
  ###Exit conversation keywords
  exit_commands = ("quit","pause","exit","goodbye","bye","later")
  ###Random starter question
  random_questions = (
        "why are you here?",
        "are there many humans like you?",
        "what do you consume for sustenance?",
        "is there intelligent life on this planet?",
        "Does Earth have a leader?",
        "What planets have younvisited?",
        "What technology do you have on this planet?"
      )
  
  def __init__(self):
    self.alienbabble = {'describe_planet_intent':r'.*\s*your planet.*',
                            'answer_why_intent':r'why\sare.*',
                            'about_intellipat':r'.*\s*intellipaat',
                             }
  def greet(self):
          self.name = input("what is your name?\n")
          will_help = input(
               f"Hi {self.name},I am Rule-Bot.will you help me learn about your planet?\n")
          if will_help in self.negetive_responses:
              print("ok, have a nice Earth day!")
              return
          self.chat()

  def make_exit(self,reply):
        for command in self.exit_commands:
            if reply == command:
                print("okay, have a nice Earth day!")
                return True
   
  def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
           reply = input(self.match_reply(reply))        

  def match_reply(self,reply):
         for key,value in self.alienbabble.items():
             intent = key
             regex_pattern = value
             found_match = re.match(regex_pattern,reply)
             if found_match and intent =='describe_planet_intent':
                 return self.describe_planet_intent()
             elif found_match and intent == 'answer_why_intent':
                 return self.answer_why_intent()
             elif found_match and intent == 'about_intellipat':
                 return self.about_intellipat()
             elif found_match and intent == 'about_session':
                 return self.about_session()
         if not found_match:
              return self.no_match_intent()
         
  def describe_planet_intent(self):
       responses = ("My planet is a utopia of diverse organisms and species.\n",
                      "I am from Opidipus,the capital of the wayward Galaxies.\n")
       return random.choice(responses)
    
  def answer_why_intent(self):
      responses = ("I come in peace\n","I am here to collect data on your planet and its inhabitants\n",
                      "I heard the coffee is good\n")
      return random.choice(responses)
    
  def about_intellipat(self):
      responses = ("Intellipaat is world's largest professional educational company\n","Intellipaat will make you learn concepts in the never learn\n",
                      "Intellipaat is where your career and skill grows\n")
      return "Intellipaat is great place to learn\n"
  
  def about_session(self):
      responses = ('session is on 14th Aug 2022\n','session was cool!!')
      return random.choice(responses)
    
  def no_match_intent(self):
         responses = (
         "Plese tell me more.\n","Tell me more!\n","Why do you say that?\n","I see. can you elaborate?\n",
         "Interesting.Can you tell me more?\n", "I see. How do you think?\n","why?\n",
         "How do you think I feel when you say that?\n")
         return random.choice(responses)
    

AlienBot = RuleBot()
AlienBot.greet()
