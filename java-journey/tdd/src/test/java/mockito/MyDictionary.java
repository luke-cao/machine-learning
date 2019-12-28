package mockito;

import java.util.Map;

public class MyDictionary {
    Map<String, String> wordMap;

    public MyDictionary(Map<String, String> wordMap) {
        this.wordMap = wordMap;
    }

    public void add(final String word, final String meaning) {
        wordMap.put(word, meaning);
    }

    public String getMeaning(final String word) {
        return wordMap.get(word);
    }
}
