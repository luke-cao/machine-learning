package calculator;

import org.junit.Before;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;
import static org.mockito.Mockito.when;

public class CalculatorTest {
    private static final long FIRST_NUMBER = 12345L;
    private static final long SECOND_NUMBER = 4567L;

    @Mock
    private NumberSource numberSource;

    @Before
    public void beforeEachTest() {
        MockitoAnnotations.initMocks(this);
        when(numberSource.fetchNextNumber()).thenReturn(FIRST_NUMBER, SECOND_NUMBER);
    }

    @Test
    public void addTwoNumbers() {
        Calculator calculator = new Calculator(numberSource);
        long result = calculator.addTwoNumbers();

        assertThat(result, is(FIRST_NUMBER + SECOND_NUMBER));

    }
}
