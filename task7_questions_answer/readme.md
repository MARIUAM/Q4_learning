# 1.) The Agent class has been defined as a dataclass why?


# `@dataclass` Python mein use hota hai jab kisi class ka main kaam sirf data store karna ho, jaise `Agent` class mein — jisme agent ki instructions, tools, aur memory hoti hain. Ye decorator automatically `__init__`, `__repr__`, aur `__eq__` jaise methods bana deta hai, isse code short, readable, aur clean rehta hai. Is tarah se hum easily ek agent object bana sakte hain bina extra boilerplate code likhe. Yani `Agent` class ek profile card ki tarah hoti hai, jisme `@dataclass` aapke liye saari basic details fill kar deta hai.


# 2a. The system prompt is contained in the Agent class as instructions? Why you can also set it as callable?

# Yeh jo Agent class hoti hai, usme system prompt ko instructions ke naam se store karte hain taake agent hamesha apni role ya personality ko yaad rakhe, jaise "aap ek helpful assistant hain." Is se baar-baar wahi baat dobara likhne ki zarurat nahi padti. Dusri baat, Agent class ko callable banana matlab usme __call__ method define karna hota hai, jis se aap agent object ko function ki tarah directly call kar sakte ho, jaise agent("Hello"). Yeh approach code ko zyada simple aur natural banata hai, jaise aap seedha agent se baat kar rahe ho, bina extra methods call kiye. Is tarah se interaction zyada smooth aur intuitive ho jata hai.


# 2b
# Jab hum Runner.run() method call karte hain, to usmein user_prompt parameter is liye diya jata hai kyunki har baar user ka input alag hota hai, aur yeh input agent ko batata hai ke user ne kya poocha hai. Is method ko @classmethod is wajah se banaya gaya hai taake humein Runner ka object banane ki zarurat na pade — hum direct class se hi method call kar saken, jaise Runner.run("Hello"). Yeh approach code ko simple, clean aur fast bana deti hai, aur agent ko run karne ka easy tareeqa provide karti hai. Is tarah, har user prompt easily handle ho jata hai bina extra code likhe.




#3.) What is the purpose of the Runner class?



# `run()` method mein user prompt is liye pass kiya jata hai kyunki har baar user ka input alag hota hai, jaise "What's the weather?" ya "Help me find a hotel." Is liye method ko har dafa naya input lena padta hai taake wo us hisaab se response de sakay.

Aur `run()` method ko `@classmethod` is liye banaya jata hai taake humein Runner class ka object banane ki zarurat na pade. Matlab seedha `Runner.run("input")` likh ke turant kaam ho jaye, bina `r = Runner()` jaisa kuch karne ke. Yeh approach code ko simple aur clean rakhti hai.

Is tarah se user input directly run method mein jata hai, aur bina object banaye Runner class se asaani se call ho jata hai. Simple aur efficient!

Agar chaho toh main iska chhota sa example bhi likh doon?


# 4.) What are generics in Python? Why we use it for TContext?


#Generics Python mein ek aisi technique hai jo humein aise classes aur functions banane ki sahulat deti hai jo kisi bhi data type ke saath kaam kar sakte hain. Isse code zyada flexible, reusable aur type-safe ban jata hai. Jaise agar hum ek Agent class banayein jo har user ka alag "context" handle kare — kabhi calendar, kabhi shopping cart, to hum TContext jaisa generic type use karte hain. Is tarah humein har context ke liye alag class nahi likhni padti, aur hum ek hi class se multiple situations ko handle kar sakte hain. Ye approach software engineering mein smart aur scalable design ka hissa hoti hai.
