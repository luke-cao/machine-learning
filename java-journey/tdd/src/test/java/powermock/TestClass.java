package powermock;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mockito;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import static org.mockito.Matchers.anyString;
import static org.mockito.Mockito.*;
import static org.powermock.api.mockito.PowerMockito.*;

@RunWith(PowerMockRunner.class)
@PrepareForTest({CollaboratorWithFinalMethods.class, CollaboratorWithStaticMethods.class, CollaboratorForPartialMocking.class})
public class TestClass {
    @Test
    public void testFinal_new() throws Exception {
        CollaboratorWithFinalMethods mock = PowerMockito.mock(CollaboratorWithFinalMethods.class);
        whenNew(CollaboratorWithFinalMethods.class).withNoArguments().thenReturn(mock);

        CollaboratorWithFinalMethods collaborator = new CollaboratorWithFinalMethods();
        verifyNew(CollaboratorWithFinalMethods.class).withNoArguments();

        PowerMockito.when(collaborator.helloMethod()).thenReturn("Hello Luke");
        String welcome = collaborator.helloMethod();
        verify(collaborator).helloMethod();
        assertThat("Hello Luke", is(welcome));
    }

    @Test(expected = RuntimeException.class)
    public void testStatic() {
        mockStatic(CollaboratorWithStaticMethods.class);
        PowerMockito.when(CollaboratorWithStaticMethods.firstMethod(anyString())).thenReturn("Hello Luke");

        String firstWelcome = CollaboratorWithStaticMethods.firstMethod("Whoever");
        String secondWelcome = CollaboratorWithStaticMethods.firstMethod("Whatever");

        assertEquals("Hello Luke", firstWelcome);
        assertEquals("Hello Luke", secondWelcome);

        PowerMockito.doThrow(new RuntimeException()).when(CollaboratorWithStaticMethods.class);
        CollaboratorWithStaticMethods.thirdMethod();
        CollaboratorWithStaticMethods.thirdMethod();

        PowerMockito.verifyStatic(CollaboratorWithStaticMethods.class, times(2));
        CollaboratorWithStaticMethods.firstMethod(anyString());
        PowerMockito.verifyStatic(CollaboratorWithStaticMethods.class, never());
        CollaboratorWithStaticMethods.secondMethod();

    }

    @Test
    public void testPartialMocking() throws Exception {
        PowerMockito.spy(CollaboratorForPartialMocking.class);
        PowerMockito.when(CollaboratorForPartialMocking.staticMethod()).thenReturn("I am a static method.");

        String returnValue = CollaboratorForPartialMocking.staticMethod();

        assertThat(returnValue, is("I am a static method."));
        verifyStatic(CollaboratorForPartialMocking.class, times(1));
        CollaboratorForPartialMocking.staticMethod();

        CollaboratorForPartialMocking collaborator = new CollaboratorForPartialMocking();
        CollaboratorForPartialMocking mock = PowerMockito.spy(collaborator);

        PowerMockito.when(mock.finalMethod()).thenReturn(("I am a final mock method"));
        returnValue = mock.finalMethod();
        Mockito.verify(mock).finalMethod();
        assertEquals("I am a final mock method", returnValue);

        PowerMockito.when(mock, "privateMethod").thenReturn("I am a private mock method.");
        returnValue = mock.privateMethodCaller();
        verifyPrivate(mock).invoke("privateMethod");
        assertEquals("I am a private mock method. Welcome to the Java world.", returnValue);
    }
}
