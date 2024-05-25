// File: frontend/App.js

import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import HomeScreen from './screens/HomeScreen';
import OrderScreen from './screens/OrderScreen';
import ChatScreen from './screens/ChatScreen';
import FeedbackScreen from './screens/FeedbackScreen';

export default function App() {
  const [currentScreen, setCurrentScreen] = useState('home');

  const handleScreenChange = (screen) => {
    setCurrentScreen(screen);
  };

  return (
    <View style={styles.container}>
      {currentScreen === 'home' && <HomeScreen handleScreenChange={handleScreenChange} />}
      {currentScreen === 'order' && <OrderScreen handleScreenChange={handleScreenChange} />}
      {currentScreen === 'chat' && <ChatScreen handleScreenChange={handleScreenChange} />}
      {currentScreen === 'feedback' && <FeedbackScreen handleScreenChange={handleScreenChange} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});