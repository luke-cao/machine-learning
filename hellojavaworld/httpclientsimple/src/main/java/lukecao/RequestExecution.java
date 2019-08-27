package lukecao;

import org.apache.http.HttpEntity;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.fluent.Content;
import org.apache.http.client.fluent.Form;
import org.apache.http.client.fluent.Request;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class HttpClient {
    public static void main(String[] args) throws IOException {
        String uri = "https://hc.apache.org/httpcomponents-client-4.5.x/tutorial/html/fundamentals.html";

        CloseableHttpClient httpclient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(uri);
        CloseableHttpResponse response1 = httpclient.execute(httpGet);
        try {
            System.out.println(response1.getStatusLine());
            HttpEntity entity1 = response1.getEntity();
            InputStream content = entity1.getContent();
            printContent(content);
            EntityUtils.consume(entity1);
        } finally {
            response1.close();
        }

        HttpPost httpPost = new HttpPost(uri);
        List<NameValuePair> nameValuePairs = new ArrayList<>();
        nameValuePairs.add(new BasicNameValuePair("login", "e650885"));
        nameValuePairs.add(new BasicNameValuePair("password", "horse07_clk"));
        httpPost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
        CloseableHttpResponse response2 = httpclient.execute(httpPost);
        try {
            System.out.println(response2.getStatusLine());
            HttpEntity entity2 = response2.getEntity();
            InputStream content = entity2.getContent();
            printContent(content);
            EntityUtils.consume(entity2);
        } finally {
            response2.close();
        }

        Content content1 = Request.Get(uri)
                .execute().returnContent();
        System.out.println(content1.asString());

        Content content2 = Request.Post(uri)
                .bodyForm(Form.form().add("username",  "vip").add("password",  "secret").build())
                .execute().returnContent();
        System.out.println(content2.asString());
    }

    private static void printContent(InputStream content) throws IOException {
        int data;
        while ((data = content.read()) != -1) {
            System.out.print((char) data);
        }
        System.out.println();
    }
}
