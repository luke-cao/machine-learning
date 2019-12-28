package injectmocks;

public class AppService3 {
    private EmailService emailService;
    private SMSService smsService;

    public boolean sendSMS(String msg) {
        return smsService.send(msg);
    }

    public boolean sendEmail(String msg) {
        return emailService.send(msg);
    }
}
