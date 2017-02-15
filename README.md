# Sentence/Line Splitter
A Python script to print random sentences and/or lines from four text files. The script uses NLTK to split the text files into separate sentences or lines, then selects a random sentence from each file and prints the results. For use in text analysis and comparison as well as digital poetics.

The script can easily be modified to include a greater or fewer number of text files. four_lines.py uses NLTK's line tokenizer to split the text files into lines, whereas four_sentences.py uses the sentence tokenizer to split the text into sentences. four_lines.py was designed to be used for poems, and four_sentences for prose. Blank lines are excluded by the line tokenizer.

## Example

Four Emily Dickinson poems--"I Felt a Funeral in My Brain," "Because I Could Not Stop for Death," "The Bustle in a House," and "Apparently with No Surprise"--were run through the four_lines.py script to produce a new stanza with random lines from each poem. The result was:

The sweeping up the heart  
For an approving God.  
A swelling of the ground;  
And Being but an ear

If the program were run again with the same textual inputs, a different stanza would be produced using lines randomly selected from each poem.





