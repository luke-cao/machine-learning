package injectmocks;

import org.junit.Before;
import org.junit.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import static org.junit.Assert.assertTrue;
import static org.mockito.Mockito.*;

public class AppServiceTest {
    @Mock
    private EmailService emailService;

    @Mock
    private SMSService smsService;

    @InjectMocks private AppService1 appService1UsingConstructor;
    @InjectMocks private AppService2 appService2UsingSetter;
    @InjectMocks private AppService3 appService3UsingField;

    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
    }

    @Test
    public void testSend() {
        when(appService3UsingField.sendEmail(anyString())).thenReturn(true);
        when(appService3UsingField.sendSMS(anyString())).thenReturn(true);

        assertTrue(appService3UsingField.sendEmail("hello"));
        assertTrue(appService3UsingField.sendSMS("world"));

        when(appService1UsingConstructor.sendEmail(anyString())).thenReturn(true);
        when(appService1UsingConstructor.sendSMS(anyString())).thenReturn(true);

        assertTrue(appService1UsingConstructor.sendEmail("hello"));
        assertTrue(appService1UsingConstructor.sendSMS("world"));

        when(appService2UsingSetter.sendEmail(anyString())).thenReturn(true);
        when(appService2UsingSetter.sendSMS(anyString())).thenReturn(true);

        assertTrue(appService2UsingSetter.sendEmail("hello"));
        assertTrue(appService2UsingSetter.sendSMS("world"));
    }
}
