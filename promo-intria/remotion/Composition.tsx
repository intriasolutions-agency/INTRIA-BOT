import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig, Sequence } from 'remotion';

const Title = ({ text, color = 'white' }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: 'clamp' });
  return (
    <div style={{
      fontSize: 80,
      fontWeight: 'bold',
      color: color,
      textAlign: 'center',
      opacity: opacity,
      fontFamily: 'Helvetica, Arial, sans-serif'
    }}>
      {text}
    </div>
  );
};

export const Main = () => {
  const { fps } = useVideoConfig();
  
  return (
    <AbsoluteFill style={{ backgroundColor: '#050505', justifyContent: 'center', alignItems: 'center' }}>
      {/* Escena 1: El Gancho */}
      <Sequence from={0} durationInFrames={fps * 5}>
        <Title text="INTRIA" color="#007bff" />
        <div style={{ color: 'white', marginTop: 20, fontSize: 30 }}>Eficiencia Radical.</div>
      </Sequence>

      {/* Escena 2: Soluciones */}
      <Sequence from={fps * 5} durationInFrames={fps * 10}>
        <Title text="SOLUCIONES A MEDIDA" />
        <div style={{ color: '#aaa', marginTop: 20, fontSize: 30 }}>Cero Relleno.</div>
      </Sequence>

      {/* Escena 3: Diferencial */}
      <Sequence from={fps * 15} durationInFrames={fps * 10}>
        <Title text="AMBICIÓN Y RESULTADOS" color="#00ffcc" />
      </Sequence>

      {/* Escena 4: CTA */}
      <Sequence from={fps * 25} durationInFrames={fps * 5}>
        <Title text="COMERNOS EL MUNDO" />
        <div style={{ color: '#007bff', marginTop: 20, fontSize: 40, fontWeight: 'bold' }}>HABLEMOS.</div>
      </Sequence>
    </AbsoluteFill>
  );
};
