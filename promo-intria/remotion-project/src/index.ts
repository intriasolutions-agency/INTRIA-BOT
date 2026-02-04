import { registerRoot, Composition } from 'remotion';
import { Main } from './Composition';
import React from 'react';

const Root = () => {
  return React.createElement(Composition, {
    id: "Main",
    component: Main,
    durationInFrames: 900,
    fps: 30,
    width: 1920,
    height: 1080,
  });
};

registerRoot(Root);
