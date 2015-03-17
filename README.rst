==============================
Feedback form demo application
==============================


Synopsis
========
This package contains a demonstration of a web-application that
presents the user a feedback-submission form.


Functional requirements
=======================
-   The application presents the visitor a form in which he can enter
    the following information:
    - name
    - email-address
    - address
    - feedback/comment

-   The application should sanitize and validate the input. Meaning:
    -   a "valid" email-address; which is something in the likes of
        ``^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$``;
        since most mail-clients do not support the full RFC email
        grammar specifications.
    -   a valid Dutch address, which consists of a street name and
        number, extension designation, a postal code in the format
        ``0000XX``.

-   The application prevents spamming.
-   The application prevents identical submits from the same user.
-   The application provides a view on all feedback submissions.


Installation
============
1.  Make sure the required dependencies are installed. These are:
    - ``pip3``
    - ``setuptools``

2.  Run ``make install``.


Running
=======
Invoke ``./run_demo``.


Usage
=====
Visit ``/`` to submit feedback and ``/list`` to view it.


Notes/Technical Debt
====================
-   There is no real concurrency model (e.g. threaded or forked) to
    handle concurrent requests.
-   System interrupts are not handled gracefully.
-   The datamodel is not properly normalized to 6NF (not really necessary).
-   The database does not enforce constraints on the postal code,
    or the country code (is assumed to be ISO 3166).
-   Django forms (used in demo.forms) are stateful, a stateless solution
    would be better.
-   CSRF protection is not implemented.
