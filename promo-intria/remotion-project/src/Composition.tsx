import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig, Sequence, spring } from 'remotion';
import React from 'react';

const DynamicTitle = ({ text, color = 'white', delay = 0, fontSize = 90 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const spr = spring({
    frame: frame - delay,
    fps,
    config: { damping: 12, stiffness: 200 },
  });

  return (
    <div style={{
      fontSize,
      fontWeight: 900,
      color: color,
      textAlign: 'center',
      transform: `scale(${spr})`,
      fontFamily: 'Impact, sans-serif',
      textTransform: 'uppercase',
      letterSpacing: '-2px',
      textShadow: '0 10px 30px rgba(0,0,0,0.5)'
    }}>
      {text}
    </div>
  );
};

const Background = () => {
  const frame = useCurrentFrame();
  const x = interpolate(frame, [0, 900], [0, 100]);
  return (
    <AbsoluteFill style={{ 
      background: `linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)`,
      zIndex: -1
    }}>
      <div style={{
        position: 'absolute',
        top: 0, left: 0, right: 0, bottom: 0,
        opacity: 0.1,
        backgroundImage: 'linear-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.1) 1px, transparent 1px)',
        backgroundSize: '50px 50px',
        transform: `translateY(-${x}px)`
      }} />
    </AbsoluteFill>
  );
};

export const Main = () => {
  const { fps } = useVideoConfig();
  
  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
      <Background />
      
      {/* Escena 1: Intro */}
      <Sequence from={0} durationInFrames={fps * 5}>
        <DynamicTitle text="INTRIA" color="#3b82f6" />
        <div style={{ 
          color: 'white', 
          marginTop: 20, 
          fontSize: 40, 
          fontFamily: 'sans-serif',
          opacity: spring({ frame: useCurrentFrame() - 10, fps, config: { damping: 100 } })
        }}>
          EFICIENCIA RADICAL
        </div>
      </Sequence>

      {/* Escena 2: Soluciones */}
      <Sequence from={fps * 5} durationInFrames={fps * 10}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
            <DynamicTitle text="SOLUCIONES" fontSize={120} />
            <DynamicTitle text="A MEDIDA" color="#00ffcc" delay={10} fontSize={120} />
        </AbsoluteFill>
      </Sequence>

      {/* Escena 3: Ambicion */}
      <Sequence from={fps * 15} durationInFrames={fps * 10}>
         <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', flexDirection: 'column' }}>
            <DynamicTitle text="RESULTADOS" color="#ff0055" />
            <div style={{ height: 20 }} />
            <DynamicTitle text="SIN EXCUSAS" color="white" delay={15} fontSize={60} />
         </AbsoluteFill>
      </Sequence>

      {/* Escena 4: CTA */}
      <Sequence from={fps * 25} durationInFrames={fps * 5}>
        <DynamicTitle text="HABLEMOS" color="#3b82f6" fontSize={150} />
      </Sequence>
    </AbsoluteFill>
  );
};
