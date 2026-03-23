import { useEffect, useState } from 'react';
import api from 'api/api';
import LoanForm from 'components/loanForm';


export default function Loans() {
  const [loans, setLoans] = useState([]);
  const [editingLoan, setEditingLoan] = useState(null);

  const fetchLoans = async () => {
    const res = await api.get('/loans');
    setLoans(res.data);
  };

  useEffect(() => {
    fetchLoans();
  }, []);

  const deleteLoan = async (id) => {
    await api.delete(`/loans/${id}`);
    fetchLoans();
  };

  return (
    <div>
      <h2>Loans</h2>

      <LoanForm
        fetchLoans={fetchLoans}
        editingLoan={editingLoan}
        setEditingLoan={setEditingLoan}
      />

      <ul>
        {loans.map((l) => (
          <li key={l.id}>
            Member {l.memberId} - {l.amount}
            <button onClick={() => setEditingLoan(l)}>Edit</button>
            <button onClick={() => deleteLoan(l.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
