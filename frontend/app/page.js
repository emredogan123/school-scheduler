"use client";

import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [conflicts, setConflicts] = useState([]);

  const fetchSchedule = async () => {
    const res = await axios.get("http://localhost:8000/schedule/grid");
    setData(res.data);
  };

  const generate = async () => {
    setLoading(true);

    const res = await axios.post("http://localhost:8000/schedule/generate");
    setConflicts(res.data.conflicts || []);

    await fetchSchedule();

    setLoading(false);
  };

  useEffect(() => {
    fetchSchedule();
  }, []);

  if (!data) return <div style={styles.loading}>Loading...</div>;

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1 style={styles.title}>📅 School Scheduler</h1>
        <button style={styles.button} onClick={generate}>
          {loading ? "Generating..." : "Generate Schedule"}
        </button>
      </div>

      {/* 🔴 Conflicts */}
      {conflicts.length > 0 && (
        <div style={styles.conflictBox}>
          <strong>⚠️ Conflicts:</strong>
          {conflicts.map((c, i) => (
            <div key={i}>
              {c.course}: {c.assigned}/{c.required}
            </div>
          ))}
        </div>
      )}

      {/* 🏫 CLASS BASED TABLES */}
      {data.classes.map((className) => (
        <div key={className} style={styles.classBlock}>
          <h2 style={styles.classTitle}>🏫 {className}</h2>

          <div style={styles.tableWrapper}>
            <table style={styles.table}>
              <thead>
                <tr>
                  <th style={styles.th}>Hour</th>
                  {data.days.map((day) => (
                    <th key={day} style={styles.th}>
                      {day}
                    </th>
                  ))}
                </tr>
              </thead>

              <tbody>
                {data.hours.map((hour) => (
                  <tr key={hour}>
                    <td style={styles.hourCell}>{hour}</td>

                    {data.days.map((day) => {
                      const cell =
                        data.grid[className]?.[hour]?.[day];

                      return (
                        <td key={day} style={styles.cell}>
                          {cell ? (
                            <div style={styles.card}>
                              <div style={styles.course}>
                                {cell.course}
                              </div>
                              <div style={styles.meta}> 👨‍🏫 Teacher : {cell.teacher}</div>
                              <div style={styles.meta}> 🏠 Classroom : {cell.classroom}</div>
                            </div>
                          ) : (
                            <div style={styles.empty}>—</div>
                          )}
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      ))}
    </div>
  );
}

const styles = {
  container: {
    padding: "40px",
    backgroundColor: "#f4f6f8",
    minHeight: "100vh",
    fontFamily: "Arial, sans-serif",
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "20px",
  },

  title: {
    fontSize: "28px",
    fontWeight: "bold",
  },

  button: {
    padding: "10px 16px",
    backgroundColor: "#2563eb",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold",
  },

  conflictBox: {
    background: "#fee2e2",
    padding: "12px",
    borderRadius: "8px",
    marginBottom: "20px",
  },

  classBlock: {
    marginBottom: "40px",
  },

  classTitle: {
    marginBottom: "10px",
  },

  tableWrapper: {
    backgroundColor: "white",
    borderRadius: "12px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
    overflow: "hidden",
  },

  table: {
    width: "100%",
    borderCollapse: "collapse",
  },

  th: {
    backgroundColor: "#e5e7eb",
    padding: "12px",
    textAlign: "left",
  },

  hourCell: {
    padding: "12px",
    fontWeight: "bold",
    borderTop: "1px solid #ddd",
  },

  cell: {
    padding: "12px",
    borderTop: "1px solid #ddd",
  },

  card: {
    backgroundColor: "#dbeafe",
    padding: "10px",
    borderRadius: "8px",
  },

  course: {
    fontWeight: "bold",
  },

  meta: {
    fontSize: "12px",
    color: "#333",
  },

  empty: {
    color: "#bbb",
  },

  loading: {
    textAlign: "center",
    marginTop: "100px",
    fontSize: "20px",
  },
};