Take the following Python code that stores a string:

```
str = 'X-DSPAM-Confidence:0.8475'
```
1. Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
2. Add 0.025 to the extracted float value to account for margin of error
3. Print the Adjusted DSPAM Confidence Score