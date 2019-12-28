package mockito;

import org.junit.Before;
import org.junit.Test;
import org.mockito.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

public class Demo {
    @Mock
    List<String> mockedList;

    @Spy
    List<String> spiedList = new ArrayList<>();

    @Captor
    ArgumentCaptor argCaptor;

    @Mock
    Map<String, String> wordMap;

    @InjectMocks
    MyDictionary dic;

    MyDictionary spiedDic ;

    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
        spiedDic = spy(new MyDictionary(wordMap));
    }

    @Test
    public void whenNotUseMockAnnotation_thenCorrect() {
        List mockList = mock(ArrayList.class);
        mockList.add("one");
        verify(mockList).add("one");
        assertEquals(0, mockList.size());

        when(mockList.size()).thenReturn(100);
        assertEquals(100, mockList.size());
    }

    @Test
    public void whenUseMockAnnotation_thenMockIsInjected() {
        mockedList.add("one");
        System.out.println(mockedList.size());

        when(mockedList.size()).thenReturn(100);
        assertEquals(100, mockedList.size());
    }

    @Test
    public void whenNotUseSpyAnnotation_thenCorrect() {
        List<String> spyList = spy(new ArrayList<>());

        spyList.add("one");
        spyList.add("two");

        verify(spyList).add("one");
        verify(spyList).add("two");

        assertEquals(2, spyList.size());

        when(spyList.size()).thenReturn(100);
        assertEquals(100, spyList.size());

        doReturn(200).when(spyList).size();
        assertEquals(200, spyList.size());
    }

    @Test
    public void whenUseSpyAnnotation_thenSpyIsInjectedCorrectly() {
        spiedList.add("one");
        spiedList.add("two");

        verify(spiedList, times(2)).add(Mockito.anyString());

        assertEquals(2, spiedList.size());

        when(spiedList.size()).thenReturn(200);
        assertEquals(200, spiedList.size());
    }

    @Test
    public void whenNotUseCaptorAnnotation_thenCorrect() {
        List mockList = mock(List.class);
        ArgumentCaptor<String> arg = ArgumentCaptor.forClass(String.class);

        mockList.add("one");
        verify(mockList).add(arg.capture());

        assertEquals("one", arg.getValue());
    }

    @Test
    public void whenUseCaptorAnnotation_thenTheSam() {
        mockedList.add("one");
        verify(mockedList, times(1)).add((String) argCaptor.capture());

        assertEquals("one", argCaptor.getValue());
    }


    @Test
    public void whenUseInjectMocksAnnotation_thenCorrect() {
        when(wordMap.get("a")).thenReturn("b");

        assertEquals("b", dic.getMeaning("a"));
    }

    @Test
    public void whenUseInjectMocksAnnotationSpy_thenCorrect() {
        when(wordMap.get("a")).thenReturn("b");

        assertEquals("b", spiedDic.getMeaning("a"));
    }

}
