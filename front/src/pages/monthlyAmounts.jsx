import { useEffect, useState } from 'react';
import api from 'api/api';
import MonthlyAmountForm from 'components/monthlyAmountForm';


export default function MonthlyAmounts() {
  const [savings, setSavings] = useState([]);
  const [editingSaving, setEditingSaving] = useState(null);

  const fetchSavings = async () => {
    const res = await api.get('/monthly-amounts');
    setSavings(res.data);
  };

  useEffect(() => {
    fetchSavings();
  }, []);

  const deleteSaving = async (id) => {
    await api.delete(`/monthly-amounts/${id}`);
    fetchSavings();
  };

  return (
    <div>
      <h2>Monthly Savings</h2>

      <MonthlyAmountForm
        fetchSavings={fetchSavings}
        editingSaving={editingSaving}
        setEditingSaving={setEditingSaving}
      />

      <ul>
        {savings.map((s) => (
          <li key={s.id}>
            Member {s.memberId} - {s.amount}
            <button onClick={() => setEditingSaving(s)}>Edit</button>
            <button onClick={() => deleteSaving(s.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
