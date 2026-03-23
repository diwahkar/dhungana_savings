
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Members from 'pages/members';
import Loans from 'pages/loans';
import MonthlyAmounts from 'pages/monthlyAmounts';

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to='/members'>Members</Link> |{' '}
        <Link to='/loans'>Loans</Link> |{' '}
        <Link to='/monthlyAmounts'>Monthly Amounts</Link>
      </nav>

      <Routes>
        <Route path='/members' element={<Members />} />
        <Route path='/loans' element={<Loans />} />
        <Route path='/monthlyAmounts' element={<MonthlyAmounts />} />
      </Routes>
    </BrowserRouter>
  );
}
