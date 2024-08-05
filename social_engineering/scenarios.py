SCENARIOS = [
    {
        'title': 'Phishing Email',
        'description': 'You receive an email that appears to be from your bank, asking you to verify your account details by clicking a link.',
        'options': [
            {'text': 'Click the link and enter your details', 'is_correct': False},
            {'text': 'Ignore the email and contact your bank directly using their official website or phone number', 'is_correct': True},
            {'text': 'Forward the email to your colleagues to warn them', 'is_correct': False},
            {'text': 'Reply to the email asking for more information', 'is_correct': False},
        ],
        'explanation': 'Banks never ask for sensitive information via email. Always verify such requests by contacting your bank directly using their official contact information.'
    },
    {
        'title': 'Tailgating',
        'description': 'A person you don\'t recognize is trying to enter the office building behind you without using their own access card.',
        'options': [
            {'text': 'Hold the door open for them', 'is_correct': False},
            {'text': 'Ask to see their employee ID and notify security if they can\'t provide one', 'is_correct': True},
            {'text': 'Ignore them and let the door close', 'is_correct': False},
            {'text': 'Call security immediately without confronting the person', 'is_correct': False},
        ],
        'explanation': 'Tailgating is a common tactic used to gain unauthorized access. Always verify the identity of individuals trying to enter secure areas.'
    },
    {
        'title': 'Suspicious Phone Call',
        'description': 'You receive a call from someone claiming to be from IT support, asking for your login credentials to fix an urgent issue.',
        'options': [
            {'text': 'Provide your username and password', 'is_correct': False},
            {'text': 'Hang up and report the incident to IT through official channels', 'is_correct': True},
            {'text': 'Give them a fake password to see what they do', 'is_correct': False},
            {'text': 'Ask them to email you instead', 'is_correct': False},
        ],
        'explanation': 'Legitimate IT support will never ask for your password. Always verify such requests through official channels.'
    },
    {
        'title': 'USB Drive Found',
        'description': 'You find a USB drive in the parking lot with your company\'s logo on it.',
        'options': [
            {'text': 'Plug it into your work computer to see what\'s on it', 'is_correct': False},
            {'text': 'Hand it over to IT or security without plugging it in', 'is_correct': True},
            {'text': 'Ask your colleagues if anyone lost a USB drive', 'is_correct': False},
            {'text': 'Plug it into your personal computer at home', 'is_correct': False},
        ],
        'explanation': 'Malicious USB drives are a common way to spread malware. Always hand found devices to IT or security without plugging them in.'
    },
    {
        'title': 'Social Media Friend Request',
        'description': 'You receive a friend request on social media from someone claiming to be a colleague, but their profile seems new and has little information.',
        'options': [
            {'text': 'Accept the request to be polite', 'is_correct': False},
            {'text': 'Ignore the request and check with your colleague in person or through a verified work channel', 'is_correct': True},
            {'text': 'Message the profile to ask why they created a new account', 'is_correct': False},
            {'text': 'Report the profile immediately as fake', 'is_correct': False},
        ],
        'explanation': 'Fake social media profiles are often used for social engineering. Always verify unexpected requests through other channels.'
    },
    {
        'title': 'Urgent Wire Transfer',
        'description': 'You receive an email appearing to be from your CEO, urgently requesting a wire transfer to a new account.',
        'options': [
            {'text': 'Process the transfer immediately as it\'s from the CEO', 'is_correct': False},
            {'text': 'Verify the request through a different communication channel, such as calling the CEO\'s office', 'is_correct': True},
            {'text': 'Reply to the email asking for more details', 'is_correct': False},
            {'text': 'Forward the email to your supervisor for guidance', 'is_correct': False},
        ],
        'explanation': 'CEO fraud is a common tactic. Always verify unusual financial requests through a different, verified communication channel.'
    },
    {
        'title': 'Phone Call from "Tech Support"',
        'description': 'You receive a call from someone claiming to be from Microsoft, saying your computer is sending out virus alerts.',
        'options': [
            {'text': 'Allow them remote access to your computer', 'is_correct': False},
            {'text': 'Hang up and report the call to your IT department or local authorities', 'is_correct': True},
            {'text': 'Provide them with your computer\'s serial number', 'is_correct': False},
            {'text': 'Ask them for a callback number to verify their identity', 'is_correct': False},
        ],
        'explanation': 'Microsoft and other tech companies don\'t make unsolicited calls about virus alerts. These are typically scams to gain access to your computer or personal information.'
    },
    {
        'title': 'Unexpected Package Delivery',
        'description': 'A delivery person arrives at your office with a package, but your receptionist is away. They ask you to sign for it.',
        'options': [
            {'text': 'Sign for the package to be helpful', 'is_correct': False},
            {'text': 'Politely decline and ask them to return when the receptionist is available', 'is_correct': True},
            {'text': 'Take the package and leave it at the receptionist\'s desk', 'is_correct': False},
            {'text': 'Open the package to check its contents', 'is_correct': False},
        ],
        'explanation': 'Unexpected deliveries can be a way to introduce unauthorized items into a secure area. Always follow proper procedures for package reception.'
    },
    {
        'title': 'Password Reset Request',
        'description': 'You receive an email requesting a password reset for an account you don\'t recognize.',
        'options': [
            {'text': 'Click the link to see what account it is', 'is_correct': False},
            {'text': 'Ignore the email and report it as phishing', 'is_correct': True},
            {'text': 'Reply to the email to clarify which account it is', 'is_correct': False},
            {'text': 'Forward the email to your IT department', 'is_correct': False},
        ],
        'explanation': 'Unexpected password reset requests are often phishing attempts. Report them as phishing and do not click any links.'
    },
    {
        'title': 'Unknown USB Drive',
        'description': 'You find an unknown USB drive in the office lobby.',
        'options': [
            {'text': 'Plug it into your work computer to see if it contains important information',
             'is_correct': False},
            {'text': 'Hand it over to IT for analysis', 'is_correct': True},
            {'text': 'Leave it where you found it', 'is_correct': False},
            {'text': 'Take it home and check it on your personal computer', 'is_correct': False},
        ],
        'explanation': 'Unknown USB drives can contain malware. Always hand them over to IT for analysis.'
    },
    {
        'title': 'Suspicious Link on Social Media',
        'description': 'A friend on social media sends you a link with a message saying "Check this out!"',
        'options': [
            {'text': 'Click the link to see what it is', 'is_correct': False},
            {'text': 'Message your friend to ask if they sent it', 'is_correct': True},
            {'text': 'Ignore the message', 'is_correct': False},
            {'text': 'Share the link with your other friends', 'is_correct': False},
        ],
        'explanation': 'Social media accounts are often hacked to spread malicious links. Verify with your friend through another channel before clicking on any links.'
    },
    {
        'title': 'Unauthorized Device on Network',
        'description': 'You notice an unknown device connected to your company\'s Wi-Fi network.',
        'options': [
            {'text': 'Ignore it as it might belong to a colleague', 'is_correct': False},
            {'text': 'Report the device to IT immediately', 'is_correct': True},
            {'text': 'Disconnect the device yourself', 'is_correct': False},
            {'text': 'Send an email to your team asking if anyone recognizes the device', 'is_correct': False},
        ],
        'explanation': 'Unknown devices on a network can be a security threat. Always report them to IT for investigation.'
    },
    {
        'title': 'Malware Warning Pop-up',
        'description': 'A pop-up appears on your computer saying it is infected with malware and provides a number to call for support.',
        'options': [
            {'text': 'Call the number provided for support', 'is_correct': False},
            {'text': 'Close the pop-up and run a virus scan using your company\'s security software',
             'is_correct': True},
            {'text': 'Click on the link in the pop-up to download the suggested antivirus', 'is_correct': False},
            {'text': 'Ignore the pop-up', 'is_correct': False},
        ],
        'explanation': 'Malware warning pop-ups are often scams. Close the pop-up and use your company\'s official security tools to scan for viruses.'
    },
    {
        'title': 'Social Media Profile Update',
        'description': 'You receive a request from a social media platform asking you to update your profile with personal details for "verification".',
        'options': [
            {'text': 'Provide the requested details', 'is_correct': False},
            {'text': 'Verify the request with the social media platform through official channels', 'is_correct': True},
            {'text': 'Ignore the request', 'is_correct': False},
            {'text': 'Update only some of the details', 'is_correct': False},
        ],
        'explanation': 'Requests for personal details can be phishing attempts. Always verify such requests through official channels.'
    },
    {
        'title': 'Conference Call Scam',
        'description': 'You receive an invitation to a conference call from an unknown source, promising valuable business insights.',
        'options': [
            {'text': 'Join the call to see what it\'s about', 'is_correct': False},
            {'text': 'Verify the source and legitimacy of the invitation before joining', 'is_correct': True},
            {'text': 'Forward the invitation to your colleagues', 'is_correct': False},
            {'text': 'Ignore the invitation', 'is_correct': False},
        ],
        'explanation': 'Unsolicited conference call invitations can be scams. Always verify the legitimacy of such invitations before participating.'
    },
    {
        'title': 'Friend’s Account Hacked',
        'description': 'A friend on social media asks you to lend them money urgently.',
        'options': [
            {'text': 'Send the money to help your friend', 'is_correct': False},
            {'text': 'Verify the request by contacting your friend through another channel', 'is_correct': True},
            {'text': 'Ignore the message', 'is_correct': False},
            {'text': 'Ask for more details before sending money', 'is_correct': False},
        ],
        'explanation': 'Urgent requests for money can be signs of hacked accounts. Verify the request by contacting your friend through another channel.'
    },
    {
        'title': 'Phony Tech Support Email',
        'description': 'You receive an email claiming to be from your company\'s IT support, asking you to download a security update.',
        'options': [
            {'text': 'Download and install the update immediately', 'is_correct': False},
            {'text': 'Verify the email with your IT department through official channels', 'is_correct': True},
            {'text': 'Reply to the email asking for more details', 'is_correct': False},
            {'text': 'Ignore the email', 'is_correct': False},
        ],
        'explanation': 'Always verify unexpected requests to download software with your IT department through official channels.'
    },
    {
        'title': 'Fake Charity Request',
        'description': 'You receive a phone call from a charity asking for a donation.',
        'options': [
            {'text': 'Donate money to support the cause', 'is_correct': False},
            {'text': 'Research the charity and donate through their official website if it\'s legitimate',
             'is_correct': True},
            {'text': 'Ask the caller for more information', 'is_correct': False},
            {'text': 'Ignore the call', 'is_correct': False},
        ],
        'explanation': 'Scammers often pose as charities to solicit donations. Always research and donate through official channels.'
    },
    {
        'title': 'Bogus Job Offer',
        'description': 'You receive an unsolicited job offer via email from a company you haven\'t applied to.',
        'options': [
            {'text': 'Respond with your personal details to learn more', 'is_correct': False},
            {'text': 'Research the company and contact them through official channels', 'is_correct': True},
            {'text': 'Ignore the email', 'is_correct': False},
            {'text': 'Forward the email to your friends who might be interested', 'is_correct': False},
        ],
        'explanation': 'Unsolicited job offers can be scams. Research the company and contact them through official channels to verify the offer.'
    },
    {
        'title': 'Free Gift Offer',
        'description': 'You receive a message on social media claiming you\'ve won a free gift and asking for your personal information to claim it.',
        'options': [
            {'text': 'Provide your personal information to claim the gift', 'is_correct': False},
            {'text': 'Ignore the message and report it as spam', 'is_correct': True},
            {'text': 'Ask for more details about the gift', 'is_correct': False},
            {'text': 'Share the message with your friends', 'is_correct': False},
        ],
        'explanation': 'Offers of free gifts in exchange for personal information are often scams. Ignore the message and report it as spam.'
    },
    {
        'title': 'Impersonation on Social Media',
        'description': 'Someone creates a social media profile pretending to be you and sends friend requests to your contacts.',
        'options': [
            {'text': 'Ignore it as a harmless prank', 'is_correct': False},
            {'text': 'Report the fake profile to the social media platform immediately', 'is_correct': True},
            {'text': 'Send a message to the impersonator asking them to stop', 'is_correct': False},
            {'text': 'Create a new profile to inform your contacts about the fake one', 'is_correct': False},
        ],
        'explanation': 'Impersonation on social media can lead to identity theft and other issues. Report the fake profile to the platform immediately.'
    },
    {
        'title': 'Fake Antivirus Software',
        'description': 'You receive a pop-up on your computer offering a free antivirus software download.',
        'options': [
            {'text': 'Download and install the antivirus software', 'is_correct': False},
            {'text': 'Close the pop-up and run a scan using your existing security software', 'is_correct': True},
            {'text': 'Ignore the pop-up', 'is_correct': False},
            {'text': 'Click on the pop-up to learn more about the antivirus software', 'is_correct': False},
        ],
        'explanation': 'Fake antivirus software can install malware on your computer. Use your existing security software to run scans and close suspicious pop-ups.'
    },
    {
        'title': 'Unrecognized Charge on Credit Card',
        'description': 'You notice an unrecognized charge on your credit card statement.',
        'options': [
            {'text': 'Ignore it as a small amount', 'is_correct': False},
            {'text': 'Report the charge to your credit card company immediately', 'is_correct': True},
            {'text': 'Call the number associated with the charge', 'is_correct': False},
            {'text': 'Wait to see if the charge is corrected next month', 'is_correct': False},
        ],
        'explanation': 'Unrecognized charges can be a sign of fraud. Report them to your credit card company immediately.'
    },
    {
        'title': 'Suspicious Job Application',
        'description': 'You receive a job application from an applicant with a resume that seems too good to be true.',
        'options': [
            {'text': 'Hire the applicant immediately', 'is_correct': False},
            {'text': 'Verify the applicant\'s credentials and references thoroughly', 'is_correct': True},
            {'text': 'Ignore any doubts and schedule an interview', 'is_correct': False},
            {'text': 'Ask the applicant for additional personal information', 'is_correct': False},
        ],
        'explanation': 'Resumes that seem too good to be true might contain false information. Verify the applicant\'s credentials and references thoroughly.'
    },
    {
        'title': 'Fake Software Update',
        'description': 'You receive a pop-up on your computer indicating a software update is available for an application you frequently use.',
        'options': [
            {'text': 'Click the pop-up to update the software immediately', 'is_correct': False},
            {'text': 'Check for updates through the application\'s official website or interface', 'is_correct': True},
            {'text': 'Ignore the pop-up', 'is_correct': False},
            {'text': 'Ask a colleague if they have received the same pop-up', 'is_correct': False},
        ],
        'explanation': 'Fake software update pop-ups can install malware. Check for updates through the application\'s official website or interface.'
    },
    {
        'title': 'Bogus Customer Service Call',
        'description': 'You receive a call from someone claiming to be from customer service, asking for your account details to resolve an issue.',
        'options': [
            {'text': 'Provide your account details to resolve the issue', 'is_correct': False},
            {'text': 'Hang up and contact customer service through the official contact information on their website',
             'is_correct': True},
            {'text': 'Ask for more information about the issue before providing details', 'is_correct': False},
            {'text': 'Ignore the call', 'is_correct': False},
        ],
        'explanation': 'Legitimate customer service representatives will not ask for sensitive information over the phone. Contact them through official channels.'
    },
    {
        'title': 'Suspicious Email Attachment',
        'description': 'You receive an email with an attachment from an unknown sender.',
        'options': [
            {'text': 'Open the attachment to see what it is', 'is_correct': False},
            {'text': 'Delete the email and report it as spam', 'is_correct': True},
            {'text': 'Forward the email to your IT department', 'is_correct': False},
            {'text': 'Reply to the sender asking for more details', 'is_correct': False},
        ],
        'explanation': 'Email attachments from unknown senders can contain malware. Delete the email and report it as spam.'
    },
    {
        'title': 'Impersonation Attempt on Phone',
        'description': 'You receive a phone call from someone claiming to be your supervisor, asking for confidential information.',
        'options': [
            {'text': 'Provide the requested information', 'is_correct': False},
            {
                'text': 'Verify the caller\'s identity through another communication channel before providing any information',
                'is_correct': True},
            {'text': 'Ask the caller for more details', 'is_correct': False},
            {'text': 'Ignore the call', 'is_correct': False},
        ],
        'explanation': 'Always verify the identity of callers asking for confidential information through another communication channel before providing any information.'
    },
]