/**
 * @param {string} s
 * @return {string}
 */
const sortSentence = (s) => {
  const splitWords = s.split(' ');
  const sortedSentence = [];
  splitWords.forEach((item) => {
    const word = item.slice(0, -1);
    const index = item.slice(-1);
    sortedSentence[index - 1] = word;
  });
  return sortedSentence.join(' ');
};