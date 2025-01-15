-------------------------------
 PyWhatKit Messaging Interface  
-------------------------------  
    This interface enables users to send messages to both individual WhatsApp numbers and WhatsApp groups seamlessly.  


Features 
----------- 
    > Send to Individuals**: Enter the recipient's phone number to send a message.  

    > Send to Groups**: Use the group's invite link to extract the required group invite code and send messages.


How It Works 
--------------
1. **Message Sending Process**:  
    - Upon initiating a message, the interface opens WhatsApp Web automatically.  
    - The message is sent after the WhatsApp Web interface completes loading and the recipient is identified.  

2. **Group Messaging**:  
   - To send a message to a WhatsApp group, you need the group's invite link.  
   - Extract the group invite code from the link (e.g., for `https://chat.whatsapp.com/your_group_invite_code`, the code is `your_group_invite_code`) and input it into the form provided by the interface.  



Notes :
-------  
    - Ensure that the WhatsApp Web interface is set up and logged in before using this tool.  
    - Make sure the internet connection is stable for smooth operation.  



Example Usage  
---------------

    - Individual Messaging: Enter the phone number in the format supported by WhatsApp (e.g., `+1XXXXXXXXXX`).  
    - Group Messaging: Extract and enter the group invite code as described above.  

This project leverages the PyWhatKit library for automated WhatsApp messaging. 
