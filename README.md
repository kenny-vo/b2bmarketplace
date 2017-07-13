# IdentiFly

## Scope
For anyone running a small to medium business, finding the right manufacturer, contractor, logistics partner, IT partner - the list goes on- has always been difficult. These folks rely on word-of-mouth recommendations, incomplete online resources or cold-calls. It's also extremely difficult to verify the credibility or reliability due to the lack of transparency.

With IdentiFly, customers will be able to post a request and have vendors come to them. They will be able to compare the costs and benefits of choosing a particular partner. This will be the online marketplace for small to medium businesses to identify partners they need, on the fly.

### Definitions
Customer(s) - a company looking for a vendor/supplier to fulfill its needs

Vendor(s) - a company looking for business

Request(s) - a request for tender a Customer makes in relation to a need

Response(s) - a tender by a Vendor in response to a particular request

## MVP
* Home page with scrollable view of active listings
* User authentication and account management
* Create requests with form validation
* Database filtering
* Contact from vendor to customer

## User Stories
* Users can view all requests in a real time reel from the home page
* Customers can create a new account
* Customers can create a Request through a form
* Customers can can review, edit or delete their older requests from their profile page
* Customers can view responses from potential Vendors
* Vendors can view details of current requests from home page
* Vendors can submit a response to a Customer regarding a particular request

## Wireframes
![Landing Page] (/Users/kennyvo/wdi/b2bmarket/main_app/static/images/landing.jpg)

## Milestones
* Database and routes created with Django
* User authentication
* Fully functional CRUD application
* Fluid navigation from Navbar
* Responsiveness

## Challenges
* Django static files
* urlpatterns
* Django packages

## Django Packages reviewed
* django-post-office
* django-postman
* django-simple-search
* djrill
* requests
* whitenoise
* django-private-chat
* django_tables2 *
* django-crispy-forms *
* djmoney *
* django-bootstrap3 *

## Future Goals
* Response form for Vendors to Customers
* Side by side comparison view of Vendor responses
* Database of all Vendors
* Review and rating system for both Vendor and Customer
