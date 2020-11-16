/* You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.
Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. 
It must return the display text as shown in the examples:

likes [] -- must be "no one likes this"
likes ["Peter"] -- must be "Peter likes this"
likes ["Jacob", "Alex"] -- must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] -- must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] -- must be "Alex, Jacob and 2 others like this"*/

function likes(names) {
    switch (names.length !== 0) {
        case true:
          if (names.length === 1) return `${names[0]} likes this`;
          names.splice(-1, 0, 'and');
          if (names.length === 3) return `${names.join(' ')} like this`;
          names[0] += ',';
          if (names.length === 4) return `${names.join(' ')} like this`;
          if (names.length > 4) {
            let num = names.length - 3;
            names = names.slice(0, 2) 
            return `${names.join(' ')} and ${num} others like this`
          }
          
        case false:
          return 'no one likes this'
    }
  }-