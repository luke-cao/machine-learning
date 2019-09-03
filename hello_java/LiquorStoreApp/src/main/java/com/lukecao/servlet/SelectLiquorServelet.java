package com.lukecao.servlet;

import com.lukecao.model.LiquorType;
import com.lukecao.service.LiquorService;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet(name = "selectliquorservlet", urlPatterns = "/SelectLiquor")
public class SelectLiquorServelet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String liquorType = req.getParameter("Type");
        LiquorService liquorService = new LiquorService();
        LiquorType l = LiquorType.valueOf(liquorType);
        List<String> liquorBrands = liquorService.getAvailableBrands(l);
        req.setAttribute("brands", liquorBrands);
        RequestDispatcher view = req.getRequestDispatcher("result.jsp");
        view.forward(req, resp);
    }
}
