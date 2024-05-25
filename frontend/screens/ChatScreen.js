// File: frontend/screens/ChatScreen.js

import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, FlatList } from 'react-native';
import { twilioAPI } from '../../payments/twilio';

const ChatScreen = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  useEffect(() => {
    // Fetch initial chat messages
    const fetchMessages = async () => {
      try {
        const messagesData = await twilioAPI.getMessages();
        setMessages(messagesData);
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    };

    fetchMessages();
  }, []);

  const sendMessage = async () => {
    try {
      await twilioAPI.sendMessage(newMessage);
      setNewMessage('');
      // Refresh messages after sending
      const messagesData = await twilioAPI.getMessages();
      setMessages(messagesData);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <View>
      <FlatList
        data={messages}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <Text>{item.text}</Text>
        )}
      />
      <TextInput
        value={newMessage}
        onChangeText={setNewMessage}
        placeholder="Type your message here"
      />
      <Button onPress={sendMessage} title="Send" />
    </View>
  );
};

export default ChatScreen;