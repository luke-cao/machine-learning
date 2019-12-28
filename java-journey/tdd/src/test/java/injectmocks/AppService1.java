package injectmocks;

public class AppService1 {
    private EmailService emailService;
    private SMSService smsService;

    public AppService1(EmailService emailService, SMSService smsSerivce) {
        this.emailService = emailService;
        this.smsService = smsSerivce;
    }

    public boolean sendSMS(String msg) {
        return smsService.send(msg);
    }

    public boolean sendEmail(String msg) {
        return emailService.send(msg);
    }
}
