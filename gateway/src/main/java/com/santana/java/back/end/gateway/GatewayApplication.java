package com.santana.java.back.end.gateway;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class GatewayApplication {

	public static void main(String[] args) {
		SpringApplication.run(GatewayApplication.class, args);
	}


	@Value("${USER_API_URL:http://app-sender:80}")
	private String app_sender;



	@Value("${PRODUCT_API_URL:http://app-receiver:80}")
	private String app_receiver;

	@Value("${SHOPPING_API_URL:http://app-orchestrating:80}")
	private String app_orchestrating;

	@Bean
	public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
		return builder.routes()
				.route("app-sender_route", r -> r.path("/app-sender/**")
						.uri(app_sender))
				.route("app-receiver_route", r -> r.path("/app-receiver/**")
						.uri(app_receiver))
				.route("app-orechestrating_route", r -> r.path("/app-orchestrating/**")
						.uri(app_orchestrating))
				.build();

	}

}
