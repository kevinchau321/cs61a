Yoda-speak translator example from lecture.

To build your own grammar, download this Treebank (25+ Mb):
http://web.mit.edu/course/6/6.863/OldFiles/share/data/corpora/treebank/combined/wsj-02-21.mrg

Then run the following commands:
cat wsj-02-21.mrg | ./rules.py | sort | ./top.py 100 4 > grammar.txt
cat wsj-02-21.mrg | ./words.py | sort | ./top.py 5 4 > lexicon.txt
./parse.py grammar.txt lexicon.txt

Example of disambiguating a known word:

the big draw of the crowd
   (NP (NP (DT the) (JJ big) (NN draw)) (PP (IN of) (NP (DT the) (NN crowd))))
They draw pictures
   (S (NP (NN They)) (VP (VB draw) (NP (NNS pictures))))

Example of disambiguating unknown words:

They twerk with the twerkiest twerkers .
   (S (NP (NN They)) (VP (VB twerk) (PP (IN with) (NP (DT the) (JJ twerkiest) (NN twerkers)))) (. .))
They ABC with the ABC ABC .
   (S (NP (NN They)) (VP (VB ABC) (PP (IN with) (NP (DT the) (JJ ABC) (NN ABC)))) (. .))
