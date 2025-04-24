import React, { useEffect, useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Heading } from '@/components/ui/heading';
import { RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, ResponsiveContainer, Legend, Tooltip } from 'recharts';

/**
 * TechRadar Component
 * 
 * Fetches metrics from GitHub API based on provided criteria and renders
 * a radar chart for technologies used across repositories.
 * 
 * Props:
 * - criteria: Array of objects defining API queries, e.g.:
 *   [{
 *     label: 'Stars',
 *     query: repo => repo.stargazers_count,
 *     color: '#8884d8',
 *   }, ...]
 * - org: GitHub organization or username to fetch repos from.
 */
export default function TechRadar({ criteria = [], org = 'your-org' }) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchRepos() {
      setLoading(true);
      try {
        const response = await fetch(`https://api.github.com/orgs/${org}/repos?per_page=100`);
        const repos = await response.json();

        // Aggregate metrics by technology (language)
        const techMap = {};
        repos.forEach(repo => {
          const lang = repo.language || 'Unknown';
          if (!techMap[lang]) techMap[lang] = { technology: lang };

          criteria.forEach(({ label, query }) => {
            const value = query(repo);
            techMap[lang][label] = (techMap[lang][label] || 0) + value;
          });
        });

        setData(Object.values(techMap));
      } catch (error) {
        console.error('Error fetching repos:', error);
      } finally {
        setLoading(false);
      }
    }

    fetchRepos();
  }, [org, criteria]);

  if (loading) {
    return (
      <Card className="p-4 shadow-lg rounded-2xl">
        <CardContent>
          <Heading level={3}>Tech Radar - Founders</Heading>
          <p>Cargando datos de GitHub...</p>
        </CardContent>
      </Card>
    );
  }

  // Determine max domain for radius axis
  const maxValue = data.reduce((max, entry) => {
    criteria.forEach(({ label }) => {
      if (entry[label] > max) max = entry[label];
    });
    return max;
  }, 0);

  return (
    <Card className="p-4 shadow-lg rounded-2xl">
      <CardContent>
        <Heading level={3} className="mb-4">Tech Radar - Founders</Heading>
        <ResponsiveContainer width="100%" height={400}>
          <RadarChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 20 }}>
            <PolarGrid />
            <PolarAngleAxis dataKey="technology" />
            <PolarRadiusAxis angle={30} domain={[0, Math.ceil(maxValue * 1.1)]} />
            {criteria.map(({ label, color }) => (
              <Radar
                key={label}
                name={label}
                dataKey={label}
                stroke={color}
                fill={color}
                fillOpacity={0.6}
              />
            ))}
            <Legend />
            <Tooltip />
          </RadarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
);
}