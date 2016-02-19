# Turbo Meme Generator Database

Download this database and change the config in your distribution of Turbo Meme Generator to reflect where the database is.

# Database guidelines
## General tag guidelines
### Our current tags
#### Simages
- "reaction" with 732 files
- "misc" with 159 files
- "food" with 106 files
- "animal" with 135 files
- "lifehack" with 61 files

#### Templates
- "animal" with 8 templates
- "any" with 192 templates
- "food" with 2 templates
- "reaction" with 73 templates

## Templates
Instead of bothering to read this section, you can use the [template designer](https://github.com/Chaquator/turbo-meme-generator-template-designer) to make the templates with ease!.

### Filenaming scheme
Looks like: `1,2,3,4,5,6,7;1,2,3,4,5,6,7`

A real-world example: `face,0,none,100 100,100 100;face,0,none,300 100,100 100,red,same;face,0,none,400 100,100 100`

- Semicolons seperate individual [entries](#entries) for templates, commas seperate sub-entries, and spaces seperate entries within sub-entries
- 1-5 are required sub-entries; the last 2 are optional
- Sub-entries:
	1. Accepted tags
		- use "any" if you want to accept literally any [simage](#simages)
	2. Tag leniency
       	- 0 or 1; where 0 represents give a simage a chance if at least _one_ tag matches, and 1 represents giving a simage a chance if it matches _all_ tags
	3. Tag blacklist
		- use "none" if there are none in the blacklist
	4. Entry's _*upper-left corner*_
	5. Entry's _*lower-right corner*_
	6. Colorize image (by arbitrary color name)
		- specify "no" if you need to use sub-sub-entry #7 without using #6
	7. Reuse same simage in following entry

## Simages
Short for "surrogate image" or "substitute image"

### Filenaming scheme
Looks like: `1,2.extension`

A real-world example: `sponge2,reaction.jpg`

- Make sure that there __IS NOT__ a space between the comma and the first tag!
- Can be any extension (`.png`, `.jpg`, whatever [Pillow](https://python-pillow.github.io/) support—know that `.gif` ends up only with its first frame being used, though)
- What the numbers mean
	1. Name to differentiate between simages with the same tags
	    - literally anything can go here
	2. Image tags
		- seperated by spaces