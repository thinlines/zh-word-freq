# Chinese word frequency

This simple Python script uses [jieba][1] to count all the words in a file and
display the most frequent ones.

Currently, it's very basic and therefore not flexible.

## Usage

```bash
./seg.py [file]
```

## Output 

(from *1984* by George Orwell)

```
温斯顿	587
可能	325
没有	323
知道	258
想	242
党	233
奥	218
布兰	210
已经	206
这种	187
```

Currently, if you don't want to see these words, or you want to see more
than ten, just edit the code. In the future, there will be a default stop
list and you'll be able to specify your own additional stop lists. See
[Current issues and goals](#current-issues-and-goals) for corresponding
issues.

## Current issues and goals

- [ ] missing argument just errs out
- [ ] add option for (multiple) stop lists
- [ ] add option to set delimiter
- [ ] add option to set number of words displayed in results

Have fun Chinese word frequencying!

## Sources

* Chinese word list copy-pasted (with modification) from [stopwords-zh][2]

[1]: https://github.com/fxsjy/jieba "Jieba Chinese text segmentation on Github"
[2]: https://github.com/stopwords-iso/stopwords-zh "List of Chinese stopwords on Github"
