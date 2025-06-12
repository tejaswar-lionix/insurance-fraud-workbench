import React, {useState} from 'react';
export const ClaimsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>CLAIMS - Claims - ingestion, parsing, validation,</h2><p>FNOL</p></div>
};
export default ClaimsView;
